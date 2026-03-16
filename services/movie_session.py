from django.db.models import QuerySet
from db.models import MovieSession


def create_movie_session(
        movie_show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )
    movie_session.save()


def get_movies_sessions(
        session_date: str = None
) -> QuerySet[MovieSession, MovieSession]:
    queryset = MovieSession.objects.all()
    if session_date:
        queryset = queryset.filter(show_time__date=session_date)
    return queryset


def get_movie_session_by_id(
        movie_session_id: int = None
) -> MovieSession:
    movie_session = MovieSession.objects.get(id=movie_session_id)
    return movie_session


def update_movie_session(
        session_id: int = None,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> None:
    session = MovieSession.objects.get(id=session_id)
    if show_time:
        session.show_time = show_time
    if cinema_hall_id:
        session.cinema_hall_id = cinema_hall_id
    if movie_id:
        session.movie_id = movie_id
    session.save()


def delete_movie_session_by_id(
        session_id: int = None
) -> None:
    MovieSession.objects.get(id=session_id).delete()
