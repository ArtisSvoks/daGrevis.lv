from uuid import uuid4
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from blog.models import *


def create_user(username=None, password=None):
    username = username if username != None else str(uuid4())
    password = password if password != None else str(uuid4())
    user = User.objects.create_user(username=username, password=password)
    return user


def create_article(user=None, title=None, content=None):
    user = user if user != None else create_user()
    title = title if title != None else str(uuid4())
    content = content if content != None else str(uuid4())
    article = Article()
    article.user = user
    article.title = title
    article.content = content
    article.save()
    return article


class ArticleTest(TestCase):
    def test_articles_list(self):
        response = self.client.get(reverse("blog_articles"))
        self.assertEqual(200, response.status_code)
        self.assertIn("No articles.", response.content)
        article1 = create_article()
        article2 = create_article()
        response = self.client.get(reverse("blog_articles"))
        self.assertIn(article1.title, response.content)
        self.assertIn(article2.content, response.content)

    def test_single_article(self):
        response = self.client.get(reverse("blog_article", kwargs={"article_pk": 9999}))
        self.assertEqual(404, response.status_code)
        article = create_article()
        response = self.client.get(reverse("blog_article", kwargs={"article_pk": article.pk}))
        self.assertEqual(200, response.status_code)
        self.assertIn(article.title, response.content)
        self.assertIn(article.content, response.content)
