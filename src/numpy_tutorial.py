# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.3
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# - [Download This Notebook](numpy_tutorial.ipynb)
# - [Numpy Documentation](https://numpy.org/doc/stable/user/index.html#user)
# - [Numpy Tutorial](https://numpy.org/doc/stable/user/absolute_beginners.html)
#
# This is an introductory tutorial for Numpy, which assumes you already know the basics of Python.  I packed a fair amount of material into it, so it's a bit of an information firehose.  If you aren't in a rush, you may learn better by reading one section a day and then experimenting with what you learned rather than blasting through in one sitting, despite how short the sections are.  Also, I've scattered relevant links to the Numpy documentation throughout in case you want more detail or an alternate framing.
#
# To begin with, we need to import Numpy.  `np` is the standard abbreviation, so we'll use that everywhere.

# %%
import numpy as np

# %% [markdown]
# Working with Arrays
# --------------------
# First, here's a few common ways to [make an array](https://numpy.org/doc/stable/reference/routines.array-creation.html).  You can turn an existing iterable (like a list) into an array, generate an array of regularly spaced numbers, create an array filled with zeros, ones, or some other number, or even generate the contents randomly (standard normal or 0-1 uniform).
# 1. `np.array(some_iterable)`
# 2. `np.linspace(start, stop, count)`, `np.logspace(start, stop, count)`
# 3. `np.zeros(shape)`, `np.ones(shape)`, `np.full(shape, value)`
# 4. `np.random.randn(shape)`, `np.random.rand(shape)`
#
# These names are mostly self-explanatory, but if you aren't sure of something, remember you can run e.g. `help(np.full)` to read the documentation.  Here is an example which creates an array of six numbers evenly spaced from zero to one:

# %%
x = np.linspace(0, 1, 6)
print(x)

# %% [markdown]
# The nice thing about Numpy arrays is that you can use operations and functions on every element in the array using a clean syntax.  This is also *much faster* than using a for loop.

# %%
y = 2.5 + 3 * np.sin(2.5 * x)
print(y)

# %% [markdown]
# Numpy has a *ton* of [functions](https://numpy.org/doc/stable/reference/routines.math.html) for these operations.  If you can't find something you're looking for, you can find even more functions in `scipy.special` (see [here](https://docs.scipy.org/doc/scipy/reference/special.html)).  Some examples are
# - `np.sin`, `np.cos`, `np.cot`, `np.arctanh`...
# - `np.exp`, `np.log`, `np.log10`...
# - `np.sqrt`, `np.cbrt`, `np.fabs`, `np.sign`...
# - `np.isfinite`, `np.isnan`, `np.isinf`...
#
# Numpy also provides a number of summary statistics that iterate over the array, such as `np.sum`, `np.mean`, `np.std`, `np.median`, `np.percentile`, and [many others](https://numpy.org/doc/stable/reference/routines.statistics.html).

# %%
print(np.mean(y), np.std(y))

# %% [markdown]
# Of course, you can also just index an array to get a particular element, the same way you would for a Python list or tuple.

# %%
print(y[2])

# %% [markdown]
# Data Types and Comparisons
# --------------------
# Numpy supports [more data types](https://numpy.org/doc/stable/reference/arrays.scalars.html#built-in-scalar-types) than just the double-precision floats we've defaulted to so far, such as integers, complex numbers, strings, and booleans.  You can specify which datatype you want when you create an array, or use `np.astype` to change the type afterwards.  Complex numbers (Numpy, like C, calls them cdouble) are actually a built in part of python, so you can specify imaginary numbers by adding `j` to the end of a number, e.g. `3.5j` and `1 + .5j`.

# %%
cx = np.linspace(-3, 3, 5, dtype="cdouble")
cy = np.sqrt(4j + cx)
print("cx:", cx)
print("cy:", cy)

# %% [markdown]
# Boolean arrays are particularly useful, as you can use them to filter your existing arrays.  The main way to do this is by comparing an array with something, and then using the resulting boolean array to index any array of the same size.  For example, here is every integer between 1 and 100 whose cos is greater than 0.9:

# %%
x = np.arange(100)
x_filtered = x[np.sin(x) > 0.9]
print(x_filtered)

# %% [markdown]
# This is extremely valuable for data processing, especially when combined with the operators `&&` (and), `||` (or), `~` (not).  Unlike the Python keywords `and`, `or`, and `not` (which raise an error), these work by comparing each element one-by-one.   Some examples:
# - `x[np.isfinite(x)]` For an array `x` with missing data marked as `NaN` or `Inf`, this filters for the entries that are neither.
# - `np.mean(y[(x > 0) && (x <= 1)])` Finds the mean of the elements of `y` where x is within the range (0, 1).
# - `y[np.abs(y_err/y) < 0.5]` If you have measurements `y` of some data with uncertainty `y_err`, you can exclude data where the relative errors is larger than 50%.

# %% [markdown]
# N-Dimensional Arrays
# --------------------
# So far, I've shown you one-dimensional arrays, meaning they only have one index and are basically equivalent to vectors in math.  Numpy can do up to a 32-dimensional arrays.  This is what the shape parameter of the array-creation functions is for -- a shape of (10, 3) means the array is two-dimensional with 10 rows and 3 columns.  Some useful functions for dealing with shapes are [here](https://numpy.org/doc/stable/reference/routines.array-manipulation.html).  The ones I use the most are:
# - `arr.ndim` gets the number of dimensions to the array
# - `arr.shape` gets the shape of the array
# - `arr.reshape(new_shape)` changes the array shape to `new_shape`,  which must have the same product (number of elements) as the old array.
# - `arr.ravel()` "unrolls" the array into one dimension
# - `arr.T` gets the transpose -- swaps the first and last axes if ndim > 2
# - `np.vstack([arr1, arr2])`, `np.hstack([arr1, arr2])` stacks columns on their first (row) or second (column) dimension.
#
# For example of a few of these together:

# %%
x = np.arange(12)
print("Setup:", x.ndim, x.shape, "\n", x)
x = x.reshape(3, 4)
print("Reshaped:", x.ndim, x.shape, "\n", x)
x = x.T
print("Transposed:", x.ndim, x.shape, "\n", x)

# %% [markdown]
# A helpful feature Numpy provides is the `axis` keyword on many of its functions that operate across a 1-d array.  This lets you select which axis to operate on, rather than flattening the array and operating on the whole thing.  For example, here's the average across each row:

# %%
np.mean(x, axis=1)

# %% [markdown]
# Broadcasting and Slicing
# --------------------
# To do an operation involving two Numpy arrays, they need to have compatible shapes.  The simplest way to do this is for them to have the same shape, but Numpy has some rules for more complicated situations it calls [broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html).  They are:
#
# 1. If the number of dimensions differs, implicitly add length-one dimensions to start of the lower-dimension array's shape until they match.  E.g. (5,) -> (1, 1, 5) if 3 dimensions are needed.
# 2. If the length of each dimension matches, operate on them element-wise (like a for loop does).  If instead one array's length in that dimension is 1, reuse it for every element of the other array.
#
# This probably sounds more complicated than it actually is, and these are incredibly useful once you get the hang of them.  Here's an example of broadcasting: 

# %%
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([-5, 10, 3])
print(a + b)

# %% [markdown]
# This works because `a` has shape (2, 3) and `b` has shape (3,).  When added, `b` is broadcast to (1, 3) following rule 1, so that `b` is added to each row of a (reusing it, following rule 2).  On the other hand, if we tried `a.T * b`, it would fail; rule 1 would again broadcast `b` to (1, 3), but this isn't compatible with `a.T`, which has shape (3, 2).  The second dimension lengths aren't equal nor is one of them 1, so Numpy will raise an exception.
#
# You might imagine this means we're going to have to use `reshape` a *ton* just to get everything to line up properly.  While it does get some use, a lot of it can be avoided by using Numpy's powerful slicing system.  Similarly to [Python slicing](https://www.geeksforgeeks.org/python/python-list-slicing/), this lets you select portions of an iterable using the indexing syntax `arr[start:stop:step]`.  For example, here is every number between 0 and 99, sliced to select every 12th element beginning with the 20th element but before the 80th:

# %%
x = np.arange(100)
print(x[20:80:12])

# %% [markdown]
# You don't have to specify any of these, since start defaults to 0 (the start of the array), stop defaults to -1 (the end), and step defaults to 1.  So `x[::]` and `x[:]` select everything (a no-op).  More interestingly, the step can be negative to work *backwards* from start to stop (meaning stop must be < start to select anything):

# %%
print(x[50:20:-8])

# %% [markdown]
# All of that is standard Python slicing.  Numpy arrays support slicing in several dimensions at once by separating the indices with commas, as in `a[1, 2]`; you can use `:` to skip an axis if you need to index later axes instead:

# %%
print(a[::-1])
print(a[:, ::-1])

# %% [markdown]
# Throwing one last wrench into things, you can also add additional length-1 dimensions as-needed with `np.newaxis`.  This lets you adjust the dimensions quickly just before broadcasting.  For example, here's how to make a multiplication table from a 1-d array (this is known as an outer product):

# %%
x = np.arange(1, 11)
print(x[:, np.newaxis] * x)

# %% [markdown]
# I could have written the second term as `x[np.newaxis, :]`, but that was unneeded due to broadcasting rule 1 (above).
#
# Combining slicing, broadcasting, filtering, and Numpy functions allow you to do some very complex operations on large amounts of data in just a few lines.  In addition to being more terse than for loops, it is also faster since Numpy's internal iteration is handled in compiled C code.

# %% [markdown]
# Linear Algebra
# --------------------
# There's a lot of interesting things you can do with multidimensional arrays, but linear algebra is central enough that I'll discuss it here (but here's the [Numpy linalg documentation](https://numpy.org/doc/stable/reference/routines.linalg.html) for good measure).
#
# Starting things off, the symbol for matrix multiplication is "@" (they were scraping the bottom of the barrel on symbols):

# %%
M = np.random.rand(3, 4)
x = np.linspace(3, 10, 4)
print(M)
print("x:", x)
print("M@x:", M @ x)

# %% [markdown]
# Notice that `x` was treated as a *column vector* despite being 1-d and printed as a row of numbers.  This is convenient, but can easily lead to confusion and programming errors, so be careful.  If you transpose x, it is *still* a column vector since the first and last dimension are the same.  Worse, if you think about how matrix multiplication works (e.g. $AB \neq BA$ in most cases), you'll see that this operation *cannot* follow the broadcasting rules described in the previous section.  To avoid confusion, you might consider making all of your vectors 2-d using `arr.reshape` or `[:, np.newaxis]`, so that it's completely clear which are row vectors and which are column vectors, and transposing works the way you'd expect.
#
# As long as you can keep that straight, Numpy is very good for doing linear algebra.  Here are a handful of particularly useful functions:
# 1. `np.dot(A, B)` computes the dot product of two matrices or vectors.
# 2. `np.cross(A, B)` computes the cross product of two vectors, so long as they are length 3 (or 2, which causes Numpy to assume the third component is zero).
# 3. `np.linalg.eye(n)` creates an $n \times n$ identity matrix 
# 3. `np.linalg.det(A)` computes the determinant of a matrix.
# 4. `np.norm(x)` computes the norm of a vector or matrix.  There's quite a few options for the type of norm, but if you use the defaults (as I have here) you'll get the length of the vector.
# 5. `np.linalg.eig(A)` computes the eigenvalues and eigenvectors of a square matrix.
# 6. `np.linalg.solve(A, x)` computes the solution to the linear system $A^{-1}x$.  You can technically use `np.linalg.inv(A) @ b` but `solve` is more numerically stable so you should use it when you have a choice.
# 7. `np.linalg.lstsq(X, y)` solves the least squares problem $X\beta = y$.
#
# Of course, there is far more than this for you to use, but these are some of the core functions.  If you can't find something you're looking for, it's probably in [Scipy Linalg](https://docs.scipy.org/doc/scipy/reference/linalg.html), which has a lot of functions for special types of matrices.
