total_likes = 0

def record_like(blog_posts):
    global total_likes
    try:
        for post in blog_posts:
            total_likes = total_likes + post['Likes']
    except KeyError:
        print('Esta mal usado lo que se ingreso en la funcion')

blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2}, {'Photos': 8, 'Comments': 1, 'Shares': 1}, {'Photos': 3, 'Likes': 19, 'Comments': 3}]

record_like(blog_posts)

#El script tira un KeyError al ejecutarlo.
#Deberia considerar errores como: Si no se ingresan diccionarios, si los diccionarios no tienen el atributo buscado y si el parametro no es recorrible