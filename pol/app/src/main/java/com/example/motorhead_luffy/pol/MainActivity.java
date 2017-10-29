package com.example.motorhead_luffy.pol;

import android.os.Handler;
import android.os.StrictMode;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

import com.android.volley.AuthFailureError;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.Charset;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MainActivity extends AppCompatActivity {
    //Lists for all sensors storing the data from the .csv file
    public List<bp> bplist = new ArrayList<bp>();
    public List<glucose> glucoselist = new ArrayList<glucose>();
    public List<fat> fatlist = new ArrayList<fat>();
    public List<heart> heartrate = new ArrayList<heart>();
    public List<sleep> sleeprate = new ArrayList<sleep>();
    public List<temp> temperature = new ArrayList<temp>();
    public int rownum =0;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        // permitting the android system to bypass any needed permissions
        if (android.os.Build.VERSION.SDK_INT > 9) {
            StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
            StrictMode.setThreadPolicy(policy);
        }
        //Reading from blood pressure data
        InputStream is = getResources().openRawResource(R.raw.bp_data);
        BufferedReader reader = new BufferedReader(
                new InputStreamReader(is, Charset.forName("UTF-8"))
        );
        String line;
        try {
            while ((line = reader.readLine()) != null) {
                String[] tokens = line.split(",");
                bp s = new bp();
                s.setT1(tokens[0]);
                s.setT2(tokens[1]);
                s.setT3(tokens[2]);
                s.setT4(tokens[3]);
                s.setT5(tokens[4]);
                s.setT6(tokens[5]);
                s.setT7(tokens[6]);
                bplist.add(s);
            }
        }
        catch (Exception ex)
        {

        }
        //Reading from blood glucose data
        InputStream iss = getResources().openRawResource(R.raw.blood_glucose_data);
        BufferedReader read = new BufferedReader(
                new InputStreamReader(iss, Charset.forName("UTF-8"))
        );
        String l;
        try {
            while ((l = read.readLine()) != null) {
                String[] tokens = l.split(",");
                glucose g = new glucose();
                g.setT1(tokens[0]);
                g.setT2(tokens[1]);
                g.setT3(tokens[2]);
                g.setT4(tokens[3]);
                g.setT5(tokens[4]);
                glucoselist.add(g);
            }
        }
        catch (Exception ex)
        {

        }
        //Reading from fat percentage
        InputStream input = getResources().openRawResource(R.raw.fat_percent);
        BufferedReader readput = new BufferedReader(
                new InputStreamReader(input, Charset.forName("UTF-8"))
        );
        String lineline;
        try {
            while ((lineline = readput.readLine()) != null) {
                String[] tokens = lineline.split(",");
                fat f = new fat();
                f.setT1(tokens[0]);
                f.setT2(tokens[1]);
                f.setT3(tokens[2]);
                f.setT4(tokens[3]);
                f.setT5(tokens[4]);
                fatlist.add(f);
            }
        }
        catch (Exception ex)
        {

        }
        //reading from heartrate
        InputStream isis = getResources().openRawResource(R.raw.heart_rate);
        BufferedReader readheart = new BufferedReader(
                new InputStreamReader(isis, Charset.forName("UTF-8"))
        );
        String lineheart;
        try {
            while ((lineheart = readheart.readLine()) != null) {
                String[] tokens = lineheart.split(",");
                heart s = new heart();
                s.setT1(tokens[0]);
                s.setT2(tokens[1]);
                s.setT3(tokens[2]);
                s.setT4(tokens[3]);
                s.setT5(tokens[4]);
                heartrate.add(s);
            }
        }
        catch (Exception ex)
        {

        }
        // Reading from sleep data
        InputStream isleep = getResources().openRawResource(R.raw.sleep_data);
        BufferedReader readsleep = new BufferedReader(
                new InputStreamReader(isleep, Charset.forName("UTF-8"))
        );

        try {
            while ((line = readsleep.readLine()) != null) {
                String[] tokens = line.split(",");
                sleep s = new sleep();
                s.setT1(tokens[0]);
                s.setT2(tokens[1]);
                s.setT3(tokens[2]);
                s.setT4(tokens[3]);
                s.setT5(tokens[4]);
                sleeprate.add(s);
            }
        }
        catch (Exception ex)
        {

        }
        // Reading the temperature data
        InputStream istemp = getResources().openRawResource(R.raw.temperature);
        BufferedReader readtemp = new BufferedReader(
                new InputStreamReader(istemp, Charset.forName("UTF-8"))
        );

        try {
            while ((line = readtemp.readLine()) != null) {
                String[] tokens = line.split(",");
                temp s = new temp();
                s.setT1(tokens[0]);
                s.setT2(tokens[1]);
                s.setT3(tokens[2]);
                s.setT4(tokens[3]);
                s.setT5(tokens[4]);
                s.setT6(tokens[5]);
                temperature.add(s);
            }
        }
        catch (Exception ex)
        {

        }
    }
    public void TRANSMIT(View view)
    {
        String personID = "a123djvbvh23fv4vfd5";                     //person using our app
        long unixTime = System.currentTimeMillis() / 1000L;
        String ut = Long.toString(unixTime);                         //Timestamp from system
        EditText editText = (EditText)findViewById(R.id.medicine);
        String value = editText.getText().toString();
        final RequestQueue queue = Volley.newRequestQueue(this);
        final String url = "http://10.10.1.169:49091";              //server address
        Map<String, String> jsonParams = new HashMap<String, String>();         //Sending the details of the person,value,timestamp in a hashmap as key-value pairs
        jsonParams.put("person_id",personID);
        jsonParams.put("value",value);
        jsonParams.put("timestamp",ut);
        //Now encoding the hashmap in a JSONobject, and sending it to server using POST method and prepare the request.
        JsonObjectRequest getRequest = new JsonObjectRequest(Request.Method.POST, url, new JSONObject(jsonParams),
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        System.out.print("Success");
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {

                    }
                }
        ) {
            @Override
            protected Map<String, String> getParams() throws AuthFailureError {
                {
                    Map<String, String> params = new HashMap<String, String>();
                    params.put("Content-Type", "application/json; charset=utf-8");      //defining the content type
                    return params;
                }
            }
        };

        queue.add(getRequest);                                                          //request added to the request queue
    }
    public void SEND(View view)
    {
        final RequestQueue queue = Volley.newRequestQueue(this);
        // transmit data until one of the empties.
        while(rownum<glucoselist.size()&&rownum<bplist.size()&&rownum<fatlist.size()&&rownum<heartrate.size()&&rownum<sleeprate.size()&&rownum<temperature.size()) {
            bp b = bplist.get(rownum);
            glucose g = glucoselist.get(rownum);
            fat f = fatlist.get(rownum);
            heart h = heartrate.get(rownum);
            sleep s = sleeprate.get(rownum);
            temp t = temperature.get(rownum);
            final String url = "http://10.10.1.169:49091";
            // prepare the hashmap,attaching all the sensor parameters
            Map<String, String> jsonParams = new HashMap<String, String>();
            jsonParams.put("bp_user", b.getT1());
            jsonParams.put("bp_value", b.getT2());
            jsonParams.put("bp_unit1", b.getT3());
            jsonParams.put("bp_timestamp", b.getT4());
            jsonParams.put("bp_fullform", b.getT5());
            jsonParams.put("bp_value1", b.getT6());
            jsonParams.put("bp_unit", b.getT7());
            jsonParams.put("glucose_value", g.getT1());
            jsonParams.put("glucose_unit", g.getT2());
            jsonParams.put("glucose_user", g.getT3());
            jsonParams.put("glucose_timestamp", g.getT4());
            jsonParams.put("glucose_fullform", g.getT5());
            jsonParams.put("fat_user", f.getT1());
            jsonParams.put("fat_timestamp", f.getT2());
            jsonParams.put("fat_value", f.getT3());
            jsonParams.put("fat_unit", f.getT4());
            jsonParams.put("fat_fullform", f.getT5());
            jsonParams.put("heart_user", h.getT1());
            jsonParams.put("heart_timestamp", h.getT2());
            jsonParams.put("heart_fullform", h.getT3());
            jsonParams.put("heart_value", h.getT4());
            jsonParams.put("heart_unit", h.getT5());
            jsonParams.put("sleep_user", s.getT1());
            jsonParams.put("sleep_value", s.getT2());
            jsonParams.put("sleep_unit", s.getT3());
            jsonParams.put("sleep_timestamp", s.getT4());
            jsonParams.put("sleep_fullform", s.getT5());
            jsonParams.put("temperature_user", t.getT1());
            jsonParams.put("temperature_method", t.getT2());
            jsonParams.put("temperature_timestamp", t.getT3());
            jsonParams.put("temperature_value", t.getT4());
            jsonParams.put("temperature_unit", t.getT5());
            jsonParams.put("temperature_fullform", t.getT6());
            rownum++;
// prepare the Request for the request queue
            JsonObjectRequest getRequest = new JsonObjectRequest(Request.Method.POST, url, new JSONObject(jsonParams),
                    new Response.Listener<JSONObject>() {
                        @Override
                        public void onResponse(JSONObject response) {
                            System.out.print("Success");
                        }
                    },
                    new Response.ErrorListener() {
                        @Override
                        public void onErrorResponse(VolleyError error) {

                        }
                    }
            ) {
                @Override
                protected Map<String, String> getParams() throws AuthFailureError {
                    {
                        Map<String, String> params = new HashMap<String, String>();
                        params.put("Content-Type", "application/json; charset=utf-8");
                        params.put("Test", "Test");
                        return params;
                    }
                }
            };

// add it to the RequestQueue
            queue.add(getRequest);
            final Handler handler = new Handler();                      //code to add a delay of 3000ms
            handler.postDelayed(new Runnable() {
                @Override
                public void run() {
                }
            }, 3000);
        }
    }

}

