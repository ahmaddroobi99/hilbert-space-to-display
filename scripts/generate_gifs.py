#!/usr/bin/env python3
"""Regenerate scientific GIFs: Bloch precession, Born sampling, free wavepacket."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "gifs")
os.makedirs(OUT, exist_ok=True)

def fig_to_pil(fig, dpi=90):
    buf = BytesIO()
    fig.savefig(buf, format="png", dpi=dpi, facecolor="white")
    buf.seek(0)
    return Image.open(buf).convert("P", palette=Image.ADAPTIVE, colors=64)

def bloch():
    frames = []
    n = 16
    for i in range(n):
        th, ph = np.pi/3, 2*np.pi*i/n
        fig = plt.figure(figsize=(4,4))
        ax = fig.add_subplot(111, projection="3d")
        ax.set_box_aspect((1,1,1))
        u = np.linspace(0, 2*np.pi, 40)
        v = np.linspace(0, np.pi, 20)
        xs = np.outer(np.cos(u), np.sin(v))
        ys = np.outer(np.sin(u), np.sin(v))
        zs = np.outer(np.ones_like(u), np.cos(v))
        ax.plot_wireframe(xs, ys, zs, color="#aaaaaa", linewidth=0.3)
        ax.plot([-1.05,1.05],[0,0],[0,0], color="#888", lw=0.7)
        ax.plot([0,0],[-1.05,1.05],[0,0], color="#888", lw=0.7)
        ax.plot([0,0],[0,0],[-1.05,1.05], color="#888", lw=0.7)
        ax.text(0,0,1.15, r"$|0\\rangle$")
        ax.text(0,0,-1.25, r"$|1\\rangle$")
        x = np.sin(th)*np.cos(ph)
        y = np.sin(th)*np.sin(ph)
        z = np.cos(th)
        ax.quiver(0,0,0,x,y,z, color="#c0392b", arrow_length_ratio=0.12, lw=2.2)
        ax.set_title(r"Bloch vector  $\\alpha|0\\rangle+\\beta|1\\rangle$")
        ax.set_axis_off()
        ax.view_init(18, 35)
        frames.append(fig_to_pil(fig, 80))
        plt.close(fig)
    frames[0].save(os.path.join(OUT,"bloch_precession.gif"), save_all=True,
                   append_images=frames[1:], duration=90, loop=0, optimize=True)

def born():
    rng = np.random.default_rng(7)
    p0, p1 = 0.64, 0.36
    shots = rng.choice([0,1], size=100, p=[p0,p1])
    frames = []
    for nshots in [0,2,6,14,30,60,100]:
        fig, ax = plt.subplots(figsize=(4.4,3.2))
        c0 = int((shots[:nshots]==0).sum())
        c1 = nshots - c0
        ax.bar([0,1],[c0,c1], color=["#1f4e79","#c45911"], width=0.55)
        ax.set_xticks([0,1], [r"$|0\\rangle$", r"$|1\\rangle$"])
        ax.set_ylim(0,80)
        ax.set_title(f"Born sampling n={nshots}")
        frames.append(fig_to_pil(fig,85))
        plt.close(fig)
    frames[0].save(os.path.join(OUT,"born_sampling.gif"), save_all=True,
                   append_images=frames[1:], duration=380, loop=0, optimize=True)

def packet():
    x = np.linspace(-12,12,300)
    frames = []
    for t in np.linspace(0,4.0,12):
        s0,k0,m=0.9,2.0,1.0
        s=s0*np.sqrt(1+(t/(2*m*s0**2))**2)
        xc=k0*t/m
        env=np.exp(-(x-xc)**2/(2*s**2))/(s**0.5)
        fig,ax=plt.subplots(figsize=(5.2,2.5))
        ax.plot(x, env*np.cos(k0*(x-xc)), color="#1f4e79", lw=1.3)
        ax.fill_between(x,0,env**2*1.6, color="#2e7d32", alpha=0.3)
        ax.set_ylim(-1.6,1.8)
        ax.set_title(fr"free packet t={t:.2f}")
        frames.append(fig_to_pil(fig,80))
        plt.close(fig)
    frames[0].save(os.path.join(OUT,"wavepacket.gif"), save_all=True,
                   append_images=frames[1:], duration=140, loop=0, optimize=True)

if __name__ == "__main__":
    bloch()
    born()
    packet()
    print("wrote GIFs to", OUT)
