from sqlalchemy.ext.declarative import declarative_base

from .db_settings import db_session


def get_sqlalchemy_model_mapping(model_class):
    metadata_model_columns = [v for v in model_class.__dict__.values() if
                              hasattr(v, 'property') and hasattr(v.property, 'columns')]
    return {v.property.columns[0].key: v.key for v in metadata_model_columns}


def to_dict(model_instance):
    """
    build instance dict representation, where the key - the column name as is in the DB table, value - the associated value from the model instance
    :param model_instance:
    :return:
    """
    mapping = model_instance.get_sqlalchemy_model_mapping()
    return {k: getattr(model_instance, v) for k, v in mapping.items()}


def to_external_dict(model_instance):
    """
    build instance dict representation, where the key - the model name as is in the model, value - the associated value from the model instance
    :param model_instance:
    :return:
    """
    mapping = model_instance.get_sqlalchemy_model_mapping()
    return {v: getattr(model_instance, v) for v in mapping.values()}


Base = declarative_base()
# add some fancy useful methods to our models
Base.to_dict = to_dict
Base.to_external_dict = to_external_dict
Base.get_sqlalchemy_model_mapping = classmethod(get_sqlalchemy_model_mapping)
metadata = Base.metadata


class BaseModel(Base):
    __abstract__ = True

    def save(self):
        db_session.add(self)
        try:
            db_session.commit()
        except Exception as exc:
            db_session.rollback()
            raise

        return self

    def update(self, **attrs):
        for attr, value in attrs.items():
            setattr(self, attr, value)
        return self.save()

    @classmethod
    def get_by_id(cls, id):
        if any(
                (isinstance(id, str) and id.isdigit(),
                 isinstance(id, (int, float))),
        ):
            return db_session.query(cls).get(int(id))
        return None

    @classmethod
    def get_by_criteria(cls, **criteria):
        return db_session.query(cls).filter_by(**criteria).first()

    def __repr__(self):
        values = ', '.join(
            '{0!s}={1!r}'.format(n, getattr(self, n))
            for n in self.__table__.c.keys() if hasattr(self, n)
        )
        return '<{}({})>'.format(self.__class__.__name__, values)
