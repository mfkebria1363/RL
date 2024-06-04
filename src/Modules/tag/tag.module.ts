import { Module } from '@nestjs/common';
import { TagService } from './tag.service';
import { TagController } from './tag.controller';

@Module({
  imports: [],
  providers: [TagService],
  controllers: [TagController]
})
export class TagModule {}
