package com.example.canvas

import android.content.Context
import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import android.util.Log
import android.view.MotionEvent
import android.view.View
import android.widget.Toast
import java.util.*

class MyView(context: Context?) : View(context) {
    private val p = Paint()
    private val r = Random()
    var layoutWidth = -1
    var layoutHeight = -1

    private val N = 4
    private val tiles = Array(N) { BooleanArray(N) { r.nextBoolean() } }
    private var tileSize = 100f
    private var padding = 10f
    private var isWin = false


    override fun onLayout(changed: Boolean, left: Int, top: Int, right: Int, bottom: Int) {
        super.onLayout(changed, left, top, right, bottom)
        layoutWidth = right - left; layoutHeight = bottom - top
    }

    override fun onDraw(canvas: Canvas?) {
        var countTiles = 0

        tileSize = (layoutWidth * 0.88 / N).toFloat()
        padding = (layoutWidth * 0.1 / N).toFloat()

        canvas?.apply {
            drawColor(Color.DKGRAY)

            for (i in 0 until N) {
                for (j in 0 until N) {
                    val tile = tiles[i][j]
                    p.color = if (tile) {
                        Color.rgb(230, 82, 79)
                    } else {
                        Color.rgb(68, 219, 116)
                    }
                    countTiles += if (tile) 1 else 0

                    drawRoundRect(
                        j * tileSize + (j + 1f) * padding,
                        i * tileSize + (i + 1f) * padding,
                        (j + 1f) * (padding + tileSize),
                        (i + 1f) * (padding + tileSize),
                        20f, 20f, p
                    )
                }
            }
        }

        isWin = countTiles == 0 || countTiles == N * N
        if (isWin) Toast.makeText(context, "Win!", Toast.LENGTH_SHORT).show()
    }

    override fun onTouchEvent(event: MotionEvent?): Boolean {
        if (isWin) return false

        event?.apply {
            if (action != MotionEvent.ACTION_DOWN) return false

            var selectRectX: Int? = null
            var selectRectY: Int? = null

            for (i in 0 until N) {
                for (j in 0 until N) {
                    val left = j * tileSize + (j + 1f) * padding
                    val top = i * tileSize + (i + 1f) * padding
                    val right = (j + 1f) * (padding + tileSize)
                    val bottom = (i + 1f) * (padding + tileSize)

                    if (x in left..right && y in top..bottom) {
                        selectRectX = i
                        selectRectY = j
                        break
                    }
                }
            }

            if (selectRectX != null && selectRectY != null) {
                changeColor(selectRectX, selectRectY)
            }
        }
        invalidate()
        return true
    }

    private fun changeColor(x: Int, y: Int) {
        tiles[x][y] = !tiles[x][y]

        for (i in 0 until N) {
            tiles[x][i] = !tiles[x][i]
            tiles[i][y] = !tiles[i][y]
        }
    }
}