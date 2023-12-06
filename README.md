# Aqua

Random sentence generator trained on KonoSuba light novel using Markov chain.

Also included is a FastAPI webserver using Aqua to generate random sentences.

Training data is based on the one used by [Kazuma](https://github.com/MarsRon/kazuma).

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

Clone the project.

```bash
$ git clone https://github.com/MarsRon/aqua
```

Create a Python virtual environment.

```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

Install libraries.

```bash
$ pip install -r requirements.txt
```

Run the test script to generate a few sentences.

```bash
$ python test.py
```

Start the FastAPI webserver.

```bash
$ python main.py
```

## Generate your own Markov chain
I've included a Jupyter notebook so that you can make your own Aqua.

See [`train.ipynb`](./train.ipynb) for more information.

## License
Distributed under the MIT License. See [`LICENSE.md`](./LICENSE.md) for more information.

## Contact

MarsRon - marsron204@gmail.com - [marsron.name.my](https://marsron.name.my)
