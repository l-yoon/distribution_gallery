from django.db import models, transaction

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # 기본 데이터베이스에 먼저 저장
        super().save(*args, **kwargs)

        # 나머지 데이터베이스에도 동일하게 저장
        for db in ['postgres', 'mysql']:
            try:
                with transaction.atomic(using=db):
                    super(Post, self).save(using=db, *args, **kwargs)
            except Exception as e:
                # 오류가 발생했을 경우 로그 출력 (혹은 원하는 방식으로 처리 가능)
                print(f"Failed to save to database {db}: {e}")

    def __str__(self):
        return self.title