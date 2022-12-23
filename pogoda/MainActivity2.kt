package com.example.myapplication

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle



import android.view.View
import android.widget.ArrayAdapter
import android.widget.Spinner

import java.util.*


class MainActivity : AppCompatActivity() {


    lateinit var citiesOuts: Array<String>
    lateinit var citiesIn: Array<String>



    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)


        citiesOuts = resources.getStringArray(R.array.citiesOuts)
        citiesIn = resources.getStringArray(R.array.citiesIn)


        val spinnerOut = findViewById<View>(R.id.citiesOuts) as Spinner;
        val adapterOut: ArrayAdapter<String> =
            ArrayAdapter<String>(this, android.R.layout.simple_spinner_item, citiesOuts)
        adapterOut.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinnerOut.adapter = adapterOut;

        val spinnerIn = findViewById<View>(R.id.citiesOuts) as Spinner;
        val adapterIn: ArrayAdapter<String> =
            ArrayAdapter<String>(this, android.R.layout.simple_spinner_item, citiesIn);
        adapterIn.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinnerIn.adapter = adapterIn;

    }
}