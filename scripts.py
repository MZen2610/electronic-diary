from datacenter.models import *
from random import choice


def fix_marks(child_name):
    schoolkid = Schoolkid.objects.filter(full_name__contains=child_name).get()
    Mark.objects.filter(schoolkid=schoolkid, points__lte=3).update(points=5)


def emove_chastisements(child_name):
    schoolkid = Schoolkid.objects.filter(full_name__contains=child_name).get()
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


def create_commendation(child_name, subject_name):
    child = Schoolkid.objects.filter(full_name__contains=child_name).get()
    lesson_subject = Lesson.objects.filter(year_of_study=child.year_of_study, group_letter=child.group_letter,
                                           subject__title=subject_name).order_by('-date').first()

    praise_text = [
        'Молодец!',
        'Отлично!',
        'Хорошо!',
        'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!',
        'Великолепно!',
        'Прекрасно!',
        'Ты меня очень обрадовал!',
        'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!',
        'Ты, как всегда, точен!',
        'Очень хороший ответ!',
        'Талантливо!',
        'Ты сегодня прыгнул выше головы!',
        'Я поражен!',
        'Уже существенно лучше!',
        'Потрясающе!',
        'Замечательно!',
        'Прекрасное начало!',
        'Так держать!',
        'Ты на верном пути!',
        'Здорово!',
        'Это как раз то, что нужно!',
        'Я тобой горжусь!',
        'С каждым разом у тебя получается всё лучше!',
        'Мы с тобой не зря поработали!',
        'Я вижу, как ты стараешься!',
        'Ты растешь над собой!',
        'Ты многое сделал, я это вижу!',
        'Теперь у тебя точно все получится!']

    com = Commendation()
    com.text = choice(praise_text)
    com.created = lesson_subject.date
    com.schoolkid = child
    com.subject = lesson_subject.subject
    com.teacher = lesson_subject.teacher
    com.save()