import os
import boto
from .basic import recursive_file_list

def download_s3_bucket(bucket_name, target, credentials=None):
    if credentials:
        conn = boto.connect_s3(*credentials)
    else:
        conn = boto.connect_s3()
    b = conn.get_bucket(bucket_name)
    L = list(b.list())
    L.sort(lambda x, y: x.name > y.name)
    L = L[::-1]
    f_suffix = '_$folder$'
    for l in L:
        n = l.name
        if n.endswith(f_suffix):
            dirname = n[:-len(f_suffix)]
            pathname = os.path.join(target, dirname)
            if not os.path.exists(pathname):
                print(n)
                os.mkdir(pathname)
        else:
            pathname = os.path.join(target, n)
            dirn = os.path.split(pathname)[0]
            if dirn and not os.path.isdir(dirn):
                print('making directory %s' % dirn)
                os.mkdirs(dirn)
            if not os.path.exists(pathname):
                print(n)
                l.get_contents_to_filename(pathname)


def upload_s3_bucket(upload_dir, bucket_name, prefix=None, credentials=None):
    L = recursive_file_list(upload_dir)
    if credentials:
        conn = boto.connect_s3(*credentials)
    else:
        conn = boto.connect_s3()
    b = conn.get_bucket(bucket_name)
    for l in L:
        if prefix is not None:
            ln = prefix + '/' + l
        else:
            ln = l
        k = b.new_key(ln)
        print(l)
        ft = os.path.splitext(l)[-1].strip('.').lower()
        k.set_contents_from_filename(l, headers={'Content-Type' : 'image/%s' % ft})
