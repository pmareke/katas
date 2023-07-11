## Description

This all about an API that registers the users of a web application. 

It is designed to practice how to identify the different responsibilities in the code and decouple them.

## Goal
There are two main objectives:
1. Part 1: decouple the code from the Framework used.
2. Part 2: decouple the code from Database and Libraries.

Start on the [views.py](src/framework/views.py)

## Part 1: decouple the code from the Framework used.
1. Run the tests.
2. Do not write Business logic on the Controllers → Instead move ALL the logic to a Use Case class.
3. Do not use the Inputs of the Framework as arguments of your Use Case class.
4. Create your own exceptions to handle errors.
5. Do not use the Framework response as the response of your Use Case class.

## Part 2: decouple the code from Database and Libraries.
For the second part of the exercise you need to repeat this 4 steps for each coupling: 
1. Define an Interface using Dependency Inversion Principle.
2. Evolve your legacy code to match the Interface.
3. Create an adapter that implements the Interface and uses the Library.
4. Remove the coupling with the infrastructure (Database and Libraries) injecting the collaborator.


## Install the dependencies

within docker

    make docker-build

## Run the tests

within docker

    make docker-tests

         
## Authors
Luis Rovirosa [@luisrovirosa](https://www.twitter.com/luisrovirosa)

Jordi Anguela [@jordianguela](https://www.twitter.com/jordianguela)
