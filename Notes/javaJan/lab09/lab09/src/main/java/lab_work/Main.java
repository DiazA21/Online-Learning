// Game File
package demo.Zlabs.Lab9;

import java.awt.*;
import java.awt.event.*;
import java.util.Timer;
import java.util.TimerTask;
import javax.swing.*;

public class Game extends Canvas {

    private Ball[] balls; // Array of 3 balls

    public Game() {
        JFrame frame = new JFrame("Bouncing Balls Game");
        this.setSize(400, 400);

        frame.add(this);
        frame.pack();
        frame.setVisible(true);

        // Initialize the balls array
        balls = new Ball[] {
            new Ball(50, 50, 20, 20, 2, 3),
            new Ball(100, 100, 30, 30, 3, 2),
            new Ball(150, 150, 25, 25, 4, 4)
        };

        // Set the world dimensions using the static method in Ball
        Ball.setWorld(300, 300);

        Timer t = new Timer();
        TimerTask tt = new TimerTask() {
            @Override
            public void run() {
                draw();
            }
        };

        t.schedule(tt, 0, 50); // Schedule the timer to call draw() every 50ms

        frame.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                t.cancel();
                tt.cancel();
                frame.dispose();
            }
        });
    }

    public void draw() {
        for (Ball b : balls) { // Move each ball
            b.move();
        }
        this.repaint();
    }

    @Override
    public void paint(Graphics g) {
        g.drawRect(0, 0, Ball.worldW, Ball.worldH); // Draw the world's rectangle
        for (Ball b : balls) {
            g.drawOval(b.x, b.y, b.w, b.h); // Draw each ball
        }
    }

    public static void main(String[] args) {
        new Game(); // Start the game
    }
}



//Ball File
package demo.Zlabs.Lab9;

public class Ball {
    public int x, y, w, h; // Ball position and size
    private int dirX, dirY; // Ball direction

    // Static world dimensions
    public static int worldW;
    public static int worldH;

    // Constructor to set all fields
    public Ball(int x, int y, int w, int h, int dirX, int dirY) {
        this.x = x;
        this.y = y;
        this.w = w;
        this.h = h;
        this.dirX = dirX;
        this.dirY = dirY;
    }

    // Constructor with default direction
    public Ball(int x, int y, int w, int h) {
        this(x, y, w, h, 1, 1); // Constructor chaining
    }

    // Static method to set world dimensions
    public static void setWorld(int w, int h) {
        worldW = w;
        worldH = h;
    }

    // Move the ball and ensure it stays within the world
    public void move() {
        x += dirX;
        y += dirY;

        // Check boundaries and reverse direction if needed
        if (x < 0) {
            x = 0;
            dirX = -dirX;
        }
        if (y < 0) {
            y = 0;
            dirY = -dirY;
        }
        if (x > worldW - w) {
            x = worldW - w;
            dirX = -dirX;
        }
        if (y > worldH - h) {
            y = worldH - h;
            dirY = -dirY;
        }
    }
}