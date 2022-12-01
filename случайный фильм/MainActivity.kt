package com.example.myapplication

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.TextView
import android:allowBackup
import android:icon
import android:roundIcon
import android:supportsRtl
import android:theme
import java.util.*

class MainActivity : AppCompatActivity() {

    lateinit var movies : Array<String>
    var countOnNextClick = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        movies = resources.getStringArray(R.array.movies)
        movies.shuffle()
        val tvTitle = findViewById<TextView>(R.id.title)
        tvTitle.text = movies[0]
        Log.d("mytag", movies[0])
    }

    fun onNextClick(view: android.view.View) {
        val tvTitle = findViewById<TextView>(R.id.title)
        when (countOnNextClick) {
            movies.size-1 -> tvTitle.text = "Фильмы кончились!"
            else -> {
                countOnNextClick++
                tvTitle.text = movies[countOnNextClick]
            }
        }
    }
    fun onClearClick(view: android.view.View) {
        val tvTitle = findViewById<TextView>(R.id.title)
        movies.shuffle()
        countOnNextClick = 0
        tvTitle.text = movies[0]
    }
}