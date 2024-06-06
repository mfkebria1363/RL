import { TypeOrmModuleOptions } from "@nestjs/typeorm";

const config: TypeOrmModuleOptions = {
    type: 'mysql',
    host: 'localhost',
    port: 3306,
    username: 'root',
    password: '#63Gor&66Isf',
    database: 'testdb',
    entities: [__dirname + '/**/*.entity.{ts, js}'],
    autoLoadEntities: true,
    synchronize: true
  }

export default config
