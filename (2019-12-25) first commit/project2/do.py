import os
import sys
import tensorflow as tf


# 관련 링크: https://blog.naver.com/PostView.nhn?blogId=complusblog&logNo=221237740617&parentCategoryNo=&categoryNo=220&viewDate=&isShowPopularPosts=false&from=postList
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'



print("Hello")
print(sys.version)

hello = tf.constant('안녕, 텐서플로우!')

# 디폴트 그래프에 현재 하나의 오퍼레이션만 있는 것을 확인할 수 있다.
# print(tf.get_default_graph().get_operations())

#
# 2019-12-25 16:27:53.343962: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2
# Traceback (most recent call last):
#   File "D:/2020/Python/1. projects/(2019-12-25) first commit/project2/do.py", line 9, in <module>
#     print(tf.get_default_graph().get_operations())
# AttributeError: module 'tensorflow' has no attribute 'get_default_graph'
#


# hello 변수는 상수 오퍼레이션이 출력하게되는 텐서를 가리케게 된다.
# 오퍼레이션 실행 전까지는 텐서의 값이 결정되지 않기 때문에 tf.constant 함수의
# 입력으로 사용한 문자열이 출력되지 않는다.
print(hello)

# 세션을 생성하며 run 메소드를 사용해야 오퍼레이션이 출력하는 텐서값을 출력해 볼 수 있다.
# UTF-8로 디코딩해야 정상적으로 한글이 출력된다.
with tf.compat.v1.Session() as sess:
    a = tf.constant(3.0)
    b = tf.constant(4.0)
    c = a+b
    print('sess run: ', sess.run(c))
sess.close()
# print(sess.run(hello).decode('UTF-8'))



