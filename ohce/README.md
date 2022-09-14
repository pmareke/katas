# Ohce

**ohce** is a console application that echoes the reverse of what you input through the console.

Even though it seems a silly application, **ohce** knows a thing or two.

- When you start **ohce**, it greets you differently depending on the current time, but only in Spanish:
  - Between 20 and 6 hours, **ohce** will greet you saying: `¡Buenas noches < your name >!`
  - Between 6 and 12 hours, **ohce** will greet you saying: `¡Buenos días < your name >!`
  - Between 12 and 20 hours, **ohce** will greet you saying: `¡Buenas tardes < your name >!`
- When you introduce a **palindrome**, **ohce** likes it and after reverse-echoing it, it adds `¡Bonita palabra!`
- **ohce** knows when to stop, you just have to write Stop! and it'll answer `Adios <your_name>`and end.

This is an example of using ohce during the morning:

```sh
$ ohce Pedro
> ¡Buenos días Pedro!
$ hola
> aloh
$ oto
> oto
> ¡Bonita palabra!
$ stop
> pots
$ Stop!
> Adios Pedro
```
