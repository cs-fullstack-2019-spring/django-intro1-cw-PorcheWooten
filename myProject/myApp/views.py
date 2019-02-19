from django.http import HttpResponse

#sets functions to return text when path is called
def index(request):
    return HttpResponse("This is a bad request. Start with the music route.")

def music(request):
    return HttpResponse("Future(future), CardiB(cardi), KeKeWyatt(keke)")
def future(request):
    return HttpResponse("Nayvadius DeMun Wilburn, known professionally as Future, is an American Grammy Award winning rapper, singer, songwriter, and record producer. Born and raised in Atlanta, Georgia, Wilburn first became involved in music as part of the Dungeon Family collective, where he was nicknamed 'the Future'. Wikipedia")

def cardi(request):
    return HttpResponse("Belcalis Marlenis Almánzar, known professionally as Cardi B, is an American rapper, singer, and songwriter. Born and raised in The Bronx, New York City, she became an Internet celebrity after several of her posts and videos went viral on Vine and Instagram. Wikipedia")
def keke(request):
    return HttpResponse("Ke'Tara Shavon 'Keke' Wyatt is an American R&B singer and television personality")