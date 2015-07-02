---
layout: post
title:  "Phalcon Jumpstart - CSS/JS Minifier"
date:   2015-05-26
description: Integrated library Minifier to minify JS and CSS files to optimize Frontend, increase page loading speed.
comments: true
---

<p class="intro">
    <span class="dropcap">I</span>
    ntegrated library Minifier to minify JS and CSS files to optimize Frontend, increase page loading speed.
</p>

Integrated library Minifier to minify JS and CSS files to optimize Frontend, increase page loading speed.

I use library minify (More at: [https://code.google.com/p/minify/](https://code.google.com/p/minify/) to help javascript and css files minify reducing system load and speed up page loading. Minify library placed in the folder ***/public/min/*** and use the configuration file config in ***/public/min/groupsConfig.php*** to make each link css/js separately for each module.

Below is the text file of framework default settings, and there are 5 group can access by 5 separate paths:

{% highlight php startinline=true %}
return array(
    'jquery' => array(
        '../plugins/jquery/jquery.js',
        '../plugins/jquery/jquery-migrate.min.js',
    ),
    'jsAdmin' => array(
        '../js/admin/modernizr.min.js',
        '../js/admin/pace.min.js',
        '../js/admin/retina.min.js',
        '../js/admin/custom.js',
        '../js/admin/toastr.min.js',
        '../js/admin/dropzone.js',
        '../js/admin/bootstrap-markdown-editor.js',
        '../js/admin/main.js',
    ),
    'jsCommon' => array(
        '../js/common/main.js',
    ),
    'cssCommon' => array(
        '../css/common/style.css',
    ),
    'cssAdmin' => array(
        '../css/admin/bootstrap-override.css',
        '../plugins/fontawesome/font-awesome.min.css',
        '../css/admin/pace.css',
        '../css/admin/chain.css',
        '../css/admin/toastr.min.css',
        '../css/admin/dropzone.css',
        '../css/admin/spf.css',
        '../css/admin/bootstrap-markdown-editor.css',
        '../css/admin/mystyle.css',
    ),
);
{% endhighlight %}

5 of 5 resource path for 5 declared above group to report in Volt template as:


{% highlight html %}
<!-- Javascript -->
<script src="{{ static_url('min/index.php?g=jquery&rev=' ~ config.jsVersion) }}"></script>
<script type="text/javascript" src="{{ static_url('min/index.php?g=jsAdmin&rev=' ~ config.jsVersion) }}"></script>
<script type="text/javascript" src="{{ static_url('min/index.php?g=jsCommon&rev=' ~ config.jsVersion) }}"></script>

<!-- CSS -->
<link href="{{ static_url('min/index.php?g=cssAdmin&rev=' ~ config.cssVersion) }}" rel="stylesheet">
<link href="{{ static_url('min/index.php?g=cssCommon&rev=' ~ config.cssVersion) }}" rel="stylesheet">
{% endhighlight %}

### MINIFICATION CACHING
You can change this mechanism in the file cached ***/public/min/config.php*** :

{% highlight php startinline=true %}
$min_cachePath = ROOT_PATH . '/../cache/minified/';
{% endhighlight %}

Or APC is enabled

{% highlight php startinline=true %}
require 'lib/Minify/Cache/APC.php';
$min_cachePath = new Minify_Cache_APC();
{% endhighlight %}

