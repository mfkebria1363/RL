import { BadRequestException, Body, Controller, Delete, InternalServerErrorException, Post } from '@nestjs/common';
import { UserService } from './user.service';
import { response } from 'express';
import { NotFoundError } from 'rxjs';

@Controller('user')
export class UserController {
    constructor (
        private readonly userService : UserService
    ){}

    @Post('register')
    async register(@Body() body: any){
        if (body.password != body.password_confirm){
            throw new BadRequestException('Passwords do not mathc!');
        }

        try {
            await this.userService.newUser({
                first_name: body.first_name,
                last_name: body.last_name,
                email: body.email,
                password: body.password
            })

            return {
                message: "New user has been inserted successfully."
            }
        } catch (error) {
            throw new InternalServerErrorException('Failed to inset new user', error);
        }
    }

    @Post('edit')
    async edit(@Body() body: any){
        try{

            await this.userService.editUser({
                email: body.email,
                first_name : body.first_name,
                last_name : body.last_name
            })

            return {
                message: "Your information has been editted successfully."
            }

        }catch(error){
            let msg = "Failed to edit user information"
            if (error.response.message){
                msg = error.response.message
            }
            throw new InternalServerErrorException(msg, error)
        }
    }

    @Delete('delete')
    async delete(@Body() body: any){
        
        try{
            await this.userService.deleteUser(body.email)
            return { message: "User has beed deleted successfully."}
        }catch(error){
            let msg = "Failed to edit user information"
            if (error.response.message){
                msg = error.response.message
            }
            throw new InternalServerErrorException(msg, error)
        }
        
        
    }
}
