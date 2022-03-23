# Deploy on Github pages

github pages is a free service for deploying any kind of static site like
*Carbon*. in this page i will descuse how to deploy your own url shortner with
github pages for free.

## Deployment

1. Fork the repo to one of your organ or your account.
   
![fork-carbon](https://s6.uupload.ir/files/1_92py.jpg)

2. open up the the setting and change the name to what do you prefer.
   in this case i will name it `goto`.

![carbon-github-rename-repo](https://s6.uupload.ir/files/2_xlvt.jpg)

3. on the setting go to `pages` section and enable pages for this repo, by click on
    save button.
> note that you should use *branch* `maseter` and directoy `docs`

![enabe-pages-cabron](https://s6.uupload.ir/files/3_45yq.jpg)

4. go to action section, and wait for depoyment.
   ![carbon](https://s6.uupload.ir/files/4_dzoq.jpg)
whene its done! open that work flow and click on the link.
![carbon](https://s6.uupload.ir/files/5_w4si.jpg)
once you open the link, you should see the index page of carbon!
![carbon-index](https://s6.uupload.ir/files/7_psvj.jpg)
**done!**

5. now you can siply add your links and just push the chnages.
   clone the repo which you forked. `git clone <Your_repo>`
   ![1](https://s6.uupload.ir/files/6_q8bk.jpg)
   ![2](https://s6.uupload.ir/files/8_5dz1.jpg)

6. `cd goto` and run carbon `python3 carbon.py`
   > in this case the name is *goto*.
   
   replace the `BASE_URL` in the `config.py` with your *github pages url*
   ![carbon](https://s6.uupload.ir/files/10_zr6r.jpg)

7. run carbon `python3 carbon.py`
   carbon will prompt a Cli and ask you for url, title and etc.
   pass all the stuff and then commit them `git add . && git commit -m 'new urls added'`.
   and in the last step, push them `git push`
   ![carbon-donate-me!](https://s6.uupload.ir/files/9_qhf1.jpg)

   you can now open the link which you just created.