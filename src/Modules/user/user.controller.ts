import { BadRequestException, Body, Controller, Delete, InternalServerErrorException, Post, Get } from '@nestjs/common';
import { UserService } from './user.service';


@Controller('users')
export class UserController {
    constructor (
        private readonly userService : UserService
    ){}


    @Get()
    async getAll(){
        
        try{
            const users = this.userService.getAll();
            return (await users).map((usr) => {
                const {first_name, last_name, email} = usr
                return {first_name, last_name, email}
        })

        }catch(error){
            throw new InternalServerErrorException("Unable to load users data.", error)
        }
    }

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
