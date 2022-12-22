package com.example.spisok2

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.ArrayAdapter
import android.widget.ListView

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val lvPeople = findViewById<ListView>(R.id.people)
        val people = arrayOf("Petya", "Vasya", "Mary") // массив неизменяем
        // TODO: сгенерировать список персон из случайных сочетаний имён и фамилий
        // TODO: создайте два string-array в ресурсах и получите список их случайных комбинаций
        val adapter = ArrayAdapter<String>(this, R.layout.item, people)
        lvPeople.adapter = adapter // задаём адаптер (посредник) для отображения данных на списке

        // пример чтения строк из ресурсов
        val sampleList = resources.getStringArray(R.array.samplelist) // функция возвращает массив
    }

    fun onAddPersonClick(view: View) {

        // TODO: реализовать добавление новых персон в список
        // имя считывать из текстового поля
        // если нужно изменять число элементов, используйте MutableList<String>
    }
}