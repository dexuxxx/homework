package com.example.myapplication
import android.view.View
import android.widget.EditText
import android.widget.TextView
import java.util.*

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

    }

    fun onClick(v: View) {
        val etA = findViewById<EditText>(R.id.numA)
        val etB = findViewById<EditText>(R.id.numB)
        val tvSum = findViewById<TextView>(R.id.sum)

        val scan = Scanner(System.`in`)
        val strA = etA.text.toString()
        val strB = etB.text.toString()

        if (!strA.isNullOrBlank() && !strB.isNullOrBlank()){
            val sum = strA.toFloat()+strB.toFloat()
            val strSum = sum.toString()
            tvSum.text=strSum
        }
        else{
            tvSum.text="введите числа"
        }
    }
}