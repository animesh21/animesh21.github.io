---
layout: post
title:  "Why Test Driven Development(TDD)?"
date:   2018-12-16 17:10:00 +0530
categories: blog post
tags: ["TDD", "Test Driven Development"]
---
This blog starts with a brief definition of Test Driven Development.
Then we recall the basic goals of programming and understand how <abbr title="Test Driven Development">TDD</abbr> 
is essential for achieving these goals. Then we'll see a very basic hands-on example of <abbr title="Test Driven Development">TDD</abbr>
in [Python](https://en.wikipedia.org/wiki/Python_(programming_language)){:target="_blank"}.

<h2>Definition</h2>

<p>
Test driven development is a style of development where you write the test cases beforehand and then run them.
What happens next? You see all your test cases failing as you've not implemented anything. Now you start
writing code to make the test cases pass and as all of the test cases pass, you're done. You've
come up with a correct version of code at the first place. Now you may refactor the code to optimize
it further and make sure that it still works correctly by running the test cases again. Fore more
information on <abbr title="Test Driven Development">TDD</abbr>, click
<a href="https://en.wikipedia.org/wiki/Test-driven_development" target="_blank">here</a>.
</p>

<h2>3 Goals of Programming</h2>


Let's get back to the basics and recall our basic goals while we're writing code:
1. The code should be correct, today and in the unknown future
2. The code should be readable for other programmers as well as future *You*
3. The code should be extensible i.e. ready to incorporate new changes without a re-write


<h4> Goal #1</h4>

<p>
We achieve this with TDD as we write the correct version of the code in the first place instead of debugging it later.
</p>

<h4> Goal #2</h4>
Usually we break the test cases into different functions with each of them explaining the aspect of
specification they are testing. This makes reading the code easier as you know what the code is expected to do
rather than reading the standalone code and guessing what it is supposed to do.
<p>
</p>

<h4> Goal #3</h4>

<p>
When you have a test suite with a decent coverage. You can extend the functionality and test it regressively
to ensure that the existing functionality is not breaking. Then add your test cases to
test the new functionality as well.
</p>

<h2> TDD Example </h2>

<p>
Most of us start to learn coding with a simple <code>print("Hello, World!")</code> program. But how do we get to know if we have
written it correctly or not? Well, it's simple, we run the program and see the result.
</p>
<p>
Then, on a later stage, if we are asked to write a program to find if <b>N</b> is a prime number or not.
We build our logic and implement it on code. To check if it's correct or not, we try it on some random inputs.
If the output is correct, we assume the program to be correct. And that's where we go wrong. We develop a habit of writing code
and then test it manually for some random inputs or some edge cases. As we get experienced with programming, we become
so confident that we omit the testing part at all. Below is one such program:
</p>

{% highlight python %}
def is_prime(n):
    """
    :param n: int, greater than or equal to 1
    :return: bool, True if n is prime else False
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(3))
#=> prints 'True'
print(is_prime(4))
#=> prints 'False'
print(is_prime(5))
#=> prints 'True'
print(is_prime(557))
#=> prints 'True'
{% endhighlight %}

<p>
I can assume it to be correct on the basis of my testing. But when I give 1 as input, it fails as shown below:
</p>

{% highlight python %}
print(is_prime(1))
#=> prints 'True'
{% endhighlight %}

<p>
Had we written test cases at the first place, we could have avoided this bug. Below is the 
<abbr title="Test Driven Development">TDD</abbr> approach for the same program. For simplicity,
I've not used Python's <a href="https://docs.python.org/3.7/library/unittest.html"><i>unittest</i></a>
module and instead wrote a simple function <code>test_is_prime</code> to test the <code>is_prime</code>
function.
<br />
Notice how we have kept the definition of <code>is_prime</code> empty on purpose.
</p>

{% highlight python %}
def is_prime(n):
    """
    :param n: int, greater than or equal to 1
    :return: bool, True if n is prime else False
    """
    pass


def test_is_prime():
    """
    Tests the function is_prime for some set of inputs -> {1, 2, 3, 4, 5, 100, 101, 557}
    """
    prime_nums = {2, 3, 5, 101, 557}
    non_prime_nums = {1, 4, 100, 553}

    for n in prime_nums:
        result = is_prime(n)
        assert result is True, "{} is a prime number while `is_prime` returned `False`".format(n)

    for n in non_prime_nums:
        result = is_prime(n)
        assert result is False, "{} is not a prime number while `is_prime` returned `True`".format(n)
    print("Tested `is_prime` on input set -> {}".format(prime_nums.union(non_prime_nums)))
    print("Ok")

test_is_prime()

#=> Output:
Traceback (most recent call last):
  File "is_prime.py", line 34, in <module>
    test_is_prime()
  File "is_prime.py", line 24, in test_is_prime
    assert result is True, "{} is a prime number while `is_prime` returned `False`".format(n)
AssertionError: 2 is a prime number while `is_prime` returned `False`
{% endhighlight %}

<p>
Let's change <code>is_prime</code> definition and run the tests again:
</p>

{% highlight python %}
def is_prime(n):
    """
    :param n: int, greater than or equal to 1
    :return: bool, True if n is prime else False
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

test_is_prime()
#=> Output:
Traceback (most recent call last):
  File "is_prime.py", line 33, in <module>
    test_is_prime()
  File "is_prime.py", line 27, in test_is_prime
    assert result is False, "{} is not a prime number while `is_prime` returned `True`".format(n)
AssertionError: 1 is not a prime number while `is_prime` returned `True`
{% endhighlight %}


<p>
Now fixing this 1 as input problem:
</p>

{% highlight python %}
def is_prime(n):
    """
    :param n: int, greater than or equal to 1
    :return: bool, True if n is prime else False
    """
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

test_is_prime()
#=> Output:
Tested `is_prime` on input set -> {1, 2, 3, 100, 101, 5, 4, 553, 557}
Ok

{% endhighlight %}

<p>
Now we can be confident that our program is working for the mentioned input set. If we ever need to 
test the funtion for some more inputs, we just need to add them to <code>test_is_prime</code>
definition. This makes testing the program an automated process which can be repeated n number of
times without any manual intervention. Also, by writing program in such a manner, we avoid the 
pain of debugging the program later as we've written the program correct in the first place.
That's why we say:
</p>

<em>Testing rocks, debugging sucks.</em>

<p>
The source code of the final version of the program that we wrote above is available below. Download and try it yourself:
</p>

[source code](/assets/scripts/is_prime.py)

You can email me any questions/suggestions regarding this blog on my email address or ping me on the networking links provided below
in the footer.
