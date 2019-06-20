import urllib.request
import gevent
from gevent import monkey

def downloader(img_name,img_url):
        req = urllib.request.urlopen(img_url)
        img_content = req.read()
        with open(img_name,"wb") as f:
            f.write(img_content)


def main():
    gevent.joinall([
        gevent.spawn(downloader,"1.jpg","http://www.pptbz.com/pptpic/UploadFiles_6909/201203/2012031220134655.jpg"),
        gevent.spawn(downloader,"2.jpg","http://www.pptok.com/wp-content/uploads/2012/08/xunguang-4.jpg")
    ])

if __name__ == '__main__':
    main()