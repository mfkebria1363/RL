import { Module } from '@nestjs/common';
import { AppController } from '@app/app.controller';
import { AppService } from '@app/app.service';
import { TagModule } from './Modules/tag/tag.module';
import { TypeOrmModule } from '@nestjs/typeorm';
import config from './ormConfig';
import { UserModule } from './Modules/user/user.module';

@Module({
  imports: [TypeOrmModule.forRoot(config),  TagModule, UserModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
