# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "manim",
# ]
# ///
from manim import *
from manim.utils.file_ops import open_file as open_media_file

class Story(Scene):
    def construct(self):

        ft = Text("Noto Sans", font="Menlo")
        self.add(ft)
        self.wait(1)
        self.remove(ft)

        square = Square()

        # some animations display mobjects, ...
        self.play(FadeIn(square))

        # ... some move or rotate mobjects around...
        self.play(Rotate(square, PI/4))

        # some animations remove mobjects from the screen
        self.play(FadeOut(square))

        self.wait(1)

if __name__ == '__main__':
    story = Story()
    story.render() # That's it!
    
    # Here is the extra step if you want to also open 
    # the movie file in the default video player 
    # (there is a little different syntax to open an image)
    open_media_file(story.renderer.file_writer.movie_file_path)

