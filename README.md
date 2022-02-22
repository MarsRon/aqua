# Aqua

Random sentence generator using Markov chain, trained on KonoSuba light novel.

Training data is based on [Kazuma](https://github.com/MarsRon/kazuma)'s.

## Example

Normal sentences:

- If that’s the case, I’ll wait for the Destroyer to pass through, and rebuild the town.
- Kazuma, warn them too… Come to think of Kazuma as a terrorist, I’ll show you just how great I can be when I get serious!
- This isn’t the capital of water and hot springs, Alcanretia?
- This way, the gate to the mortal world… Keep this a secret, okay?
- When the guild judges the quest to defeat the Demon King to me.

Short sentences:

- Can you do that, I’ll share some mana with me!
- I might look like a devil!
- You defeated two Demon King’s army is here!
- … Is… Is that so?
- No matter how you look at it, isn’t this a rifle?

## Usage

Feel free to ~~steal~~ take inspiration from this project in any way you want, it's under MIT license so you can do whatever you want ;)

Clone the project

```bash
$ git clone https://github.com/MarsRon/aqua
```

Create a Python virtual environment

```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

Install dependencies

```bash
$ pip install -r requirements.txt
```

Run the test script to generate a few sentences

```bash
$ python test.py
```

Start the API server

```bash
$ python main.py
```

## Generate Markov chain from scratch

Go through [`Aqua.ipynb`](./Aqua.ipynb)
