import { Injectable } from '@nestjs/common';

@Injectable()
export class TagService {

    getAll():string[] {
        return  ['Human', 'Car', 'plane']
    }

}
