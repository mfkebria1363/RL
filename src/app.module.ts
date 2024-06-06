import { Module } from '@nestjs/common';
import { AppController } from '@app/app.controller';
import { AppService } from '@app/app.service';
import { TagModule } from './Modules/tag/tag.module';
import { DbmModule } from './Modules/dbm/dbm.module';

@Module({
  imports: [TagModule, DbmModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
