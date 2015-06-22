---
layout: post
title:  "Installation PhalconPHP Jumpstart"
date:   2014-06-20
---

<p class="intro">
    <span class="dropcap">I</span>
    n this post, i will be guide you how to clone and install that framework on your machine.
</p>

## Requirements
* Apache >= 2.0
* Enable Apache mod_rewrite
* PhalconPHP Framwork >=1.3.4
* PHP >=5.4 (extension: Pdo, mbstring, openssl)
* Sphinx Search Engine 2.2.+ ((Optional))
* [Sphinx Search](http://sphinxsearch.com/) (Optional)
* libODBC x64 install CentOS: yum install unixODBC unixODBC-devel postgresql-libs (dependencies of SphinxSE)

## Supported Image Libraries
* GD Library (>=2.0)
* Imagick PHP extension (>=6.5.7)

## Supported Crypt Libraries (using for encrypt cookie)
* PHP-mcrypt Extension

### CONFIGURE WEBSITE
On first clone this source from github, open file ***/conf/global.php*** and change MySQL connect information.

{% highlight php startinline=true %}
'app_db'          => [
    'adapter'     => 'Mysql',
    'host'        => 'localhost',
    'username'    => 'root',
    'password'    => 'root',
    'name'        => 'phalconjumpstart',
    'prefix'      => 'fly_'
]
{% endhighlight %}

Defined website base path to your site domain

{% highlight php startinline=true %}
'app_baseUri'     => 'newpj.site',
'app_resourceUri' => 'newpj.site',
{% endhighlight %}

Then open file ***/public/index.php*** to change cookie domain and default timezone

{% highlight php startinline=true %}
date_default_timezone_set('Asia/Bangkok');
ini_set('session.cookie_domain', '.newpj.site');
{% endhighlight %}

### START THE INSTALLATION
Open a browser and type the path to the website that you have configured in the ***/conf/global.php*** file above. For example, enter path ***http://newpj.site*** and you will be see button ***Install*** on home page then click it.

<figure>
    <img src="{{ '/uploads/pj/phalcon-jumpstart-installation.png' | prepend: site.baseurl }}" alt="">
    <figcaption>Fig1. - Phalcon Jumpstart installation page.</figcaption>
</figure>

Follow step by step to complete installation.
Have fun.



