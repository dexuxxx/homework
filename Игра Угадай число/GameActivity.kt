package com.example.myapplication

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.TextView

class GameActivity : AppCompatActivity() {
    var min:Int = 0
    var max:Int = 0
    var mean:Int = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_game)
        min = intent.getIntExtra("min", 0)
        max = intent.getIntExtra("max", 1000)
        mean = (min + max) / 2
        findViewById<TextView>(R.id.question).text = "Is your number less to $mean?"
    }

    fun onYesNoClick(view: android.view.View) {
        when (view.id) {
            R.id.yes -> {
                max = mean
                mean = (max + min) / 2
                findViewById<TextView>(R.id.question).text = "Is your number less to $mean?"
            }
            R.id.no -> {
                min = mean
                mean = (max + mean) / 2
                findViewById<TextView>(R.id.question).text = "Is your number less to $mean?"
            }
        }
        if (max - 1 == min) {
            findViewById<TextView>(R.id.question).text = "Your number is $min"
        }
    }

}