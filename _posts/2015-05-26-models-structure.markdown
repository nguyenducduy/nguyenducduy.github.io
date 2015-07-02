---
layout: post
title:  "Phalcon Jumpstart - Models Structure"
date:   2015-05-26
description: Model of Framework class undertake major processing operations as well as the functionality of the website. Model is the only class in the MVC 3 class direct access to the database to ensure the maintenance and expansion of the MVC pattern.
comments: true
---

<p class="intro">
    <span class="dropcap">M</span>odel of Framework class undertake major processing operations as well as the functionality of the website. Model is the only class in the MVC 3 class direct access to the database to ensure the maintenance and expansion of the MVC pattern.
</p>

Because it is built on object-oriented model should each be designed as one PHP class and placed in the folder ***/models/***. The Model can gather in groups for easier use Model, inheritance and maintenance. In Admin Panel Code Generator function, helps you from a table in the database, generate a model class with methods and attributes essential to be able to use right model for your Web application.

Phalcon Jumpstart used [Phalcon Model Annotations](http://docs.phalconphp.com/en/latest/reference/annotations.html) to mapping model class to table in MySQL database.

For example: the product functionality, the product will have a model containing all the related handling products that access to the database, following the syntax.

{% highlight php startinline=true %}
<?php
namespace Model;

/**
 * Product
 *
 * Represents a Product
 *
 * @Source('fly_product');
 */
class Product extends \Fly\BaseModel
{
    /**
    * @Column(type="integer", nullable=true, column="u_id")
    */
    public $uid;

    /**
    * @Primary
    * @Identity
    * @Column(type="integer", nullable=false, column="p_id")
    */
    public $id;

    /**
    * @Column(type="string", nullable=true, column="p_name")
    */
    public $name;

    ...
{% endhighlight %}

* @Source: declare table name.
* @Column:
    * type: define type of table field.
    * nullable: validate table field is NULL or NOT NULL.
    * column: table field name.

After declare the model like above, you can call model properties without prefix of table (automatic column mapping) field like:

{% highlight php startinline=true %}
    $myProduct = new \Model\Product();
    $myProduct->name = 'Product One';
    $myProduct->uid = 1;
{% endhighlight %}
