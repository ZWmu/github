import json
from django.views import View
from django.http import JsonResponse
from github.models import Author, Book
from django.middleware.csrf import get_token

# /Authors/
class Authors(View):
    def post(self, request):
        # 获取body数据
        req_dict = json.loads(request.body.decode())
        name = req_dict.get('name')
        gender = req_dict.get('gender')
        born_date = req_dict.get('born_date')

        # 校验参数
        if not all([name, gender]):
            return JsonResponse({'code': 400,
                                 'message': '缺少必传参数'})

        # 捕获异常，存入数据库
        try:
            autoer = Author.objects.create(Name=name, Gender=gender, Born_Date=born_date)
        except Exception as e:
            return JsonResponse({'code': 400,
                                 'message': '操作失败'})

        return JsonResponse({'code': 200,
                             'message': '操作成功'})

# /Books/
class Books(View):
    def post(self, request):
        # 获取body数据
        req_dict = json.loads(request.body.decode())
        author = req_dict.get('author')
        publish_date = req_dict.get('publish_date')
        country = req_dict.get('country')

        # 校验参数
        if not all([author, publish_date, country]):
            return JsonResponse({'code': 400,
                                 'message': '缺少必传参数'})

        # 捕获异常，存入数据库
        try:
            book = Book.objects.create(author=author, publish_date=publish_date, country=country)
        except Exception as e:
            return JsonResponse({'code': 400,
                                 'message': '操作失败'})

        return JsonResponse({'code': 200,
                             'message': '操作成功'})

# /Authors/name/
class AuthorsOL(View):
    def get(self, request, name):
        '''获取指定名字的作者信息'''
        # 查询数据库
        try:
            author = Author.objects.get(Name=name)
        except Exception as e:
            return JsonResponse({'code': 400,
                                 'message': '操作失败'})
        author_dict = {
            'name': author.Name,
            'gender': author.Gender,
            'bron_date': author.Bron_Date
        }
        return JsonResponse({'code': 200,
                             'message': author_dict})


# /Books/name/
class BooksOL(View):
    def get(self, request, bookname):
        '''获取指定书籍的名字'''
        # 查询数据库
        try:
            book = Book.objects.get(BookName=bookname)
        except Exception as e:
            return JsonResponse({'code': 400,
                                 'message': '操作失败'})
        book_dict = {
            'bookname': book.BookName,
            'author': book.Author,
            'publish_date': book.Publish_Date,
            'country': book.Country
        }
        return JsonResponse({'code': 200,
                             'message': book_dict})

