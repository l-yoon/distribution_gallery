# config/database_routers.py

class MultiDBRouter:
    """
    A router to control all database operations.
    - Writes will be saved to all databases: SQLite, PostgreSQL, and MySQL.
    - Reads will be attempted from default first, then PostgreSQL, then MySQL.
    """

    def db_for_read(self, model, **hints):
        # 읽기 시도 순서: default -> postgres -> mysql
        return 'default'  # 기본적으로 'default'에서 읽기를 시도합니다.

    def db_for_write(self, model, **hints):
        # 쓰기 작업은 기본적으로 'default'로 지정하지만, 이를 이용해 수동으로 다수 데이터베이스에 쓰도록 구성할 것입니다.
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow any relation if both models are in the same database.
        """
        db_set = {'default', 'postgres'} ##, 'mysql'
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Allow migrations on all databases.
        """
        return True