package com.example.myapplication

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.EditText

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }

    fun onNextIntent(view: View) {
        val intent = Intent(applicationContext, GameActivity::class.java)
        intent.putExtra("min", findViewById<EditText>(R.id.min).text)
        intent.putExtra("max", findViewById<EditText>(R.id.max).text)
        startActivity(intent)
    }
}