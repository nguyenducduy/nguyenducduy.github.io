---
layout: post
title:  "Phalcon Jumpstart - Multi Language Structure"
date:   2015-05-26
description: Each controller will have one particular language file, the file name of the form.
comments: true
---

<p class="intro">
    <span class="dropcap">E</span>
    ach controller will have one particular language file, the file name of the form: controller.php (eg product.php, user.php ...).
</p>

DECLARE

Interface language are saved as PHP file and placed in the folder ***/language/*** . Each controller will have one particular language file, the file name of the form: controller.php (eg product.php, user.php ...)

The subfolders of the folder language (eg en, vn ...) is the package language (Language Code). In the language package, a controller shall be declared in the php file, so all of the action of controller that will get data that language. And the language files are located in folders named with module.

SYNTAX

Contents of 1 php file includes language information variable name and corresponding value chains. For example:

{% highlight php startinline=true %}
<?php
return [
    'VARIABLE' => 'VALUE_VARIABLE',
    'name_not_empty' => 'Product name is required.',
    'name_is_unique' => 'Product name already existed. Please choose another.'
];
{% endhighlight %}

* VARIABLE: The variable name is used to access to this value
* VALUE_VARIABLE: the respective value chains to show to the outside interface.

INITIALIZE

Information of the language service was created in ***Bootstrap.php*** file located at ***/libs/Fly/Bootstrap.php***:

{% highlight php startinline=true %}
//Setting language service
$this->di->setShared('lang', function() use ($dispatcher, $cookie) {
    $language = '';

    // Detect language via cookie
    if ($cookie->has('language')) {
        $language = $cookie->get('language')->getValue();
    } else {
        //Get default language
        $language = $this->config->defaultLanguage;
    }

    return new \Fly\Translate\Adapter\Native([
        'module' => strtolower($dispatcher->getModuleName()),
        'controller' => $dispatcher->getControllerName(),
        'language' => $language
    ]);
});
{% endhighlight %}

When you need access to the language service in treatment of one controller action is as follows:

{% highlight php startinline=true %}
$this->lang->get('name_not_empty');
{% endhighlight %}

or in Volt

{% highlight html %}
{% raw %}
{{ lang.get('name_not_empty') }}
{% endraw %}
{% endhighlight %}

