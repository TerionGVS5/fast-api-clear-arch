Robert Cecil Martin:
> the database is a detail

> the framework is a detail

There are three layers.
1.  Buisness logic (entities and use cases)
2.  Storage. Now we use postgresql, but we can easy change to something else. For example, third party api. **Because buisness logic don't depend from Storage.**
3. Rest. It is our external layer. Now it is FastAPI. Similarly we can use other web framework. Not even necessarily a web.

All in docker-compose :smile: that's why easy to run and to use.

*ORM - SQLAlchemy. For generation migration Alembic, not so cool as Django Migration, but better that manual.*
