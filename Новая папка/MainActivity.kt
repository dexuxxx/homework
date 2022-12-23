package com.example.pogoda

import android.annotation.SuppressLint
import android.os.AsyncTask
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import org.json.JSONException
import org.json.JSONObject
import java.io.BufferedReader
import java.io.IOException
import java.io.InputStreamReader
import java.net.HttpURLConnection
import java.net.MalformedURLException
import java.net.URL
import java.io.InputStream


class MainActivity : AppCompatActivity() {
    // Поля, что будут ссылаться на объекты из дизайна
    lateinit var user_field: EditText
    lateinit var main_btn: Button
    lateinit var result_info: TextView
    override fun onCreate(savedInstanceState: Bundle?) { // Сработает при создании Activity
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)


        user_field = findViewById(R.id.user_field)
        main_btn = findViewById(R.id.main_btn)
        result_info = findViewById(R.id.result_info)

        // Обработчик нажатия на кнопку
        main_btn.setOnClickListener(View.OnClickListener {

            if (user_field.getText().toString()
                    .trim { it <= ' ' } == ""
            ) Toast.makeText(this@MainActivity, R.string.no_user_input, Toast.LENGTH_LONG)
                .show() else {

                val city = user_field.getText().toString()
                val key = "d949c43a681d5a7f37f907d7bc0e377f"
                val url =
                    "https://api.openweathermap.org/data/2.5/weather?q=\" + city + \"&appid=\" + d949c43a681d5a7f37f907d7bc0e377f + \"&units=metric&lang=ru\n"

                GetURLData().execute(url)
            }
        })
    }

    @SuppressLint("StaticFieldLeak")
    private inner class GetURLData: AsyncTask<String, String, String>() {

        override fun onPreExecute() {
            super.onPreExecute()
            result_info!!.text = "Ожидайте..."
        }

        // Будет выполняться во время подключения по URL
        protected override fun doInBackground(vararg strings: String): String? {
            var connection: HttpURLConnection? = null
            var reader: BufferedReader? = null
            try {

                val url = URL(strings[0])
                connection = url.openConnection() as HttpURLConnection
                connection.connect()


                val stream = connection!!.inputStream
                reader = BufferedReader(InputStreamReader(stream))


                val buffer = StringBuilder()
                var line: String? = ""


                while (reader.readLine().also { line = it } != null) buffer.append(line)
                    .append("\n")


                return buffer.toString()
            } catch (e: MalformedURLException) {
                e.printStackTrace()
            } catch (e: IOException) {
                e.printStackTrace()
            } finally {

                connection?.disconnect()
                try {
                    reader?.close()
                } catch (e: IOException) {
                    e.printStackTrace()
                }
            }
            return null
        }

        // Выполняется после завершения получения данных
        @SuppressLint("SetTextI18n")
        override fun onPostExecute(result: String?) {
            super.onPostExecute(result)


            try {
                val jsonObject = JSONObject(result)
                result_info!!.text =
                    "Температура: " + jsonObject.getJSONObject("main").getDouble("temp")
            } catch (e: JSONException) {
                e.printStackTrace()
            }
        }
    }
}






