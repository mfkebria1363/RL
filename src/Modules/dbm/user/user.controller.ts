import { BadRequestException, Body, Controller, InternalServerErrorException, Post } from '@nestjs/common';
import { UserService } from './user.service';
import { response } from 'express';

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
            console.log(error)
            throw new InternalServerErrorException('Failed to inset new user', error);
        }
    }
}
