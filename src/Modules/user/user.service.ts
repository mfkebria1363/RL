import { Injectable, NotFoundException } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { User } from '../../Entities/user.entity';
import { Repository } from "typeorm";


@Injectable()
export class UserService {
    constructor(
        @InjectRepository(User) protected readonly userReopsitory: Repository<User> 
    ){}

    getAll(){
        return this.userReopsitory.find();
    }

    newUser(body: any){
        return this.userReopsitory.save(body) 
    }

    async editUser(body: any){
        const user = await this.userReopsitory.findOneBy({ email: body.email });
        if (!user){
            throw new NotFoundException(`User ${body.email} not found.`)
        }

        user.first_name = body.first_name
        user.last_name = body.last_name
        
        return this.userReopsitory.save(user);

    }

    async deleteUser(email: string){
        const res = await this.userReopsitory.delete({email})
        if (res.affected === 0){
            throw new NotFoundException(`Unable to delete user ${email} `)
        }
        return res
    }
}

