import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { User } from './user.entity';
import { Repository } from "typeorm";
import { response } from 'express';

@Injectable()
export class UserService {
    constructor(
        @InjectRepository(User) protected readonly userReopsitory: Repository<User> 
    ){}


    newUser(body: any){
        return this.userReopsitory.save(body) 
    }
}

