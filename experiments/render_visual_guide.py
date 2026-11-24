"""Build the static GitHub lesson figures with Pillow."""
from math import cos, exp, log
from PIL import Image, ImageDraw
from render_proof_figures import FAINT, INK, ORANGE, OUT, PAPER, TEAL, font


def page(width, height):
    image = Image.new("RGB", (width, height), PAPER)
    return image, ImageDraw.Draw(image)


def label(draw, x, y, text, size=26, color=INK, anchor="lm"):
    draw.text((x, y), text, font=font(size), fill=color, anchor=anchor)


def arrow(draw, x, y, end):
    draw.line((x, y, x, end), fill=TEAL, width=4)
    draw.polygon([(x-8, end-10), (x+8, end-10), (x, end)], fill=TEAL)


def proof_map():
    image, draw = page(760, 365)
    for y, title, detail in [
        (14, "Chain of theta lifts", "Build multiplicity; bound the arithmetic cost."),
        (139, "Estimate for a smoothed prime-power count", "Control the error as the cutoff X grows."),
        (264, "Location of the zeta zeros", "The analytic argument yields the critical line.")]:
        draw.rounded_rectangle((16, y, 744, y+86), radius=10, outline=TEAL, width=3)
        label(draw, 35, y+27, title, 29)
        label(draw, 35, y+62, detail, 24)
        if y < 264:
            arrow(draw, 380, y+87, y+122)
    return image


def zeros():
    image, d = page(860, 420)
    label(d, 25, 28, "Critical strip", 30)
    label(d, 350, 28, "Contribution divided by √x", 30)
    left, right, top, bottom = 30, 273, 75, 316
    for beta, tick in [(0,"0"), (.5,"½"), (1,"1")]:
        x = left + (right-left)*beta
        d.line((x,top,x,bottom),fill=TEAL if beta == .5 else FAINT,width=3)
        label(d,x,bottom+25,tick,24,anchor="mm")
    d.line((left,bottom,right,bottom),fill=INK,width=2)
    label(d,150,389,"real part β",24,anchor="mm")
    for beta, color, cy, name in [(.5,TEAL,131,"β = 0.5"),(.7,ORANGE,286,"β = 0.7   hypothetical")]:
        x=left+(right-left)*beta
        d.ellipse((x-7,178-7,x+7,178+7),fill=color)
        label(d,350,cy-54,name,24,color)
        d.line((350,cy,822,cy), fill=FAINT,width=2)
        for sign in (-1,1):
            for i in range(0,472,10):
                amp=17*exp((beta-.5)*5*i/472)
                d.line((350+i,cy+sign*amp,354+i,cy+sign*amp),fill=color,width=2)
        points=[]
        for i in range(473):
            t=5*i/472
            points.append((350+i,cy-17*exp((beta-.5)*t)*cos(4*t)))
        d.line(points,fill=color,width=3)
    label(d,350,380,"0",22)
    label(d,822,380,"5",22,anchor="rm")
    label(d,585,380,"log x",24,anchor="mm")
    return image


def weights():
    image,d=page(760,410)
    primes={2:2,3:3,4:2,5:5,7:7,8:2,9:3}
    for y, title, smoothed in [(160,"Prime-power weight   Λ(n)",False),(347,"After multiplying by 10/n − 1",True)]:
        label(d,26,y-124,title,28)
        d.line((40,y,720,y),fill=INK,width=2)
        for n in range(1,11):
            x=52+(n-1)*72
            if n in primes:
                value=log(primes[n])*(10/n-1 if smoothed else 1)
                d.rectangle((x-12,y-32*value,x+12,y-1),fill=ORANGE if primes[n]==2 else TEAL)
            label(d,x,y+20,str(n),21,anchor="mm")
    label(d,380,394,"n",22,anchor="mm")
    return image


def lifts():
    image,d=page(740,480)
    for i,(group,caption) in enumerate([
        ("0", "Start with an automorphic form."),
        ("1", "The first lift supplies a new form."),
        ("2", "Use the output as the next input."),
        ("m", "After m lifts, exploit multiplicity m.")]):
        y=45+116*i
        d.rounded_rectangle((20,y-27,184,y+27),radius=9,outline=TEAL,width=3)
        label(d,56,y,"U(X",32)
        label(d,111,y+9,group,20)
        label(d,130,y,")",32)
        label(d,208,y,caption,24)
        if i<3:
            arrow(d,102,y+32,y+83)
            label(d,208,y+58,"Further lifts …" if i==2 else "Pair through a theta kernel",21,TEAL)
    label(d,20,454,"Across the chain: track divisibility and sizes of lifts.",25)
    return image


def divisibility():
    image, draw = page(640, 420)
    a, b = 3, 2
    for step in range(3):
        y = 52 + 120 * step
        label(draw, 22, y, ["Input", "One pass", "Two passes"][step], 29)
        draw.rounded_rectangle((212, y-31, 378, y+31), radius=9, outline=TEAL, width=3)
        label(draw, 295, y, f"({a}, {b})", 33, anchor="mm")
        odd = a % 2 or b % 2
        label(draw, 398, y, "Odd entry" if odd else "Both even", 27,
              INK if odd else TEAL)
        if step < 2:
            arrow(draw, 295, y+34, y+86)
            label(draw, 318, y+61, "sum, difference", 23)
        a, b = a+b, a-b
    draw.line((22, 353, 616, 353), fill=FAINT, width=3)
    label(draw, 22, 385, "Divide (6, 4) by 2 to recover (3, 2).", 28)
    return image


def divisibility_window():
    image, draw = page(660, 440)
    center, unit = 330, 30
    for row, level in enumerate((2, 3)):
        top = 18 + 208 * row
        axis = top + 101
        bound = level * 3
        label(draw, 24, top + 18, f"{level} classes: total size at most {bound}", 28)
        draw.line((center-10*unit, axis, center+10*unit, axis), fill=INK, width=2)
        draw.rectangle((center-bound*unit, axis-12, center+bound*unit, axis+12),
                       fill=FAINT, outline=TEAL, width=2)
        for value in (-8, 0, 8):
            x = center + value * unit
            inside = abs(value) <= bound
            draw.ellipse((x-8, axis-8, x+8, axis+8), fill=INK if inside else PAPER,
                         outline=INK, width=3)
            label(draw, x, axis+35, str(value), 25, anchor="mm")
        label(draw, 24, top+171, "Only 0 fits." if bound < 8 else "−8, 0 and 8 fit.", 26, TEAL)
    return image


if __name__ == "__main__":
    for name, render in [("proof-map",proof_map),("critical-strip",zeros),
                         ("smoothed-weights",weights),("theta-chain",lifts),
                         ("lift-divisibility", divisibility),
                         ("divisibility-window", divisibility_window)]:
        render().save(OUT / (name + ".png"))
