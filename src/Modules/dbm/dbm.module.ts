import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { UserModule } from './user/user.module';
import { DbmController } from './dbm.controller';
import { DbmService } from './dbm.service';

@Module({
    imports:[
        TypeOrmModule.forRoot({
            type: 'mysql',
            host: 'localhost',
            port: 3306,
            username: 'root',
            password: '#63Gor&66Isf',
            database: 'testdb',
            autoLoadEntities: true,
            synchronize: true
          }),
        UserModule,
    ],
    controllers: [DbmController],
    providers: [DbmService]
})
export class DbmModule {}
