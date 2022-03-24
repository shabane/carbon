# Deploy with nginx

> as you know you should have nginx installed on your server.

1. open up a config file for carbon in `/etc/nginx/conf.d/` directory. i will call it `carbon.conf`

   `vim /etc/nginx/conf.d/carbon.conf`

2. clone the carbon project to directory which you choose. i prefer to use `/var/`

   `cd /var && git clone https://github.com/shabane/carbon.git`

3. create the configuration for the server.

```nginx
server {
        listen 80;
        root /var/carbon/docs;
        index index.html;
        server_name carbon.ir; # use your server name or leave it as comment.

        
        location ~ / {
                try_files $uri
                rewrite /* $uri.html;
        }
}
```

> note that i use my domain for it, absolutly you should use yours to work.