from crypt import methods
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['GET'])

def home():
    girl = """\
         /_________________________________________________________________/|\
        l                                                                 || \
        l   ,-,__.              #            #                  #         ||
        l  { / ,__\                                                       ||
        l { `}'- -/    #               #             #                  # ||
        l {`}'\ o/                                                        ||
        l  U__J  L__   C'mon - it's wide open; surely you can stick it in!||
        l .'   `' ._`.                                                    ||
        l/ /; o )  o) \        #                #                 #       ||
        / / \`~' `;'} :                                                   ||
        : {   )    (/ /                     #                 #            ||
        \ \ /   .  )/                                                     ||
        l\ Y      l/                #                 #              #    ||
        l Y    \#/ \                                                      ||
        l {     \  | .....................................................||..
        l  \     \ |                                                      ||
        l   `.    \;                                                      ||
        l     `.   \                                                      ||
        l       |)  :                                                     ||
        .l......./  /......................................................|'..
                : /
                / /{
            / /_`-,
            (_ \_~^^
                `~~
    """
    return girl


if __name__ == "__main__":
    app.run(debug=True)
    