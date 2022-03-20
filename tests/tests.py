import pytest
from utils import PostOperator

data = "data/data.json"
comments = "data/comments.json"

class TestPostOperator:
    def test_get_posts_all(self):
        post = PostOperator(data, comments)
        assert post.get_posts_all() == list

