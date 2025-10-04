import 'package:flutter/material.dart';

void main() {
  const title = "Uber";
  runApp(
    MaterialApp(
      title: title,
      theme: ThemeData.dark(),
      home: MyHomePage(title: title)
    )
  );
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {

  @override
  Widget build(BuildContext context) {
    // This method is rerun every time setState is called, for instance as done
    // by the _incrementCounter method above.
    //
    // The Flutter framework has been optimized to make rerunning build methods
    // fast, so that you can just rebuild anything that needs updating rather
    // than having to individually change instances of widgets.
    return Scaffold(
      appBar: AppBar(
        // TRY THIS: Try changing the color here to a specific color (to
        // Colors.amber, perhaps?) and trigger a hot reload to see the AppBar
        // change color while the other colors stay the same.
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
        title: Text(widget.title),
      ),
      body: Center(
        // Center is a layout widget. It takes a single child and positions it
        // in the middle of the parent.
        child: SizedBox(
          width: 400,
      child: const DebugForm()
        )
        )
    );
  }
}


class DebugForm extends StatefulWidget {
  const DebugForm({super.key});

  @override
  State<DebugForm> createState() => _DebugFormState();
}

class _DebugFormState extends State<DebugForm> {
  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();

  TimeOfDay? _time;
  final TextEditingController _timeController = TextEditingController();
  final TextEditingController _idController = TextEditingController();

  void submit(TimeOfDay time, int driverID) {

  }

  @override
  Widget build(BuildContext context) {
    return Form(
      key: _formKey,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: <Widget>[
          Row(
              children: <Widget>[
              Expanded(
              child: TextFormField(
                controller: _timeController,
                readOnly: true,
                decoration: const InputDecoration(
                  hintText: 'Time'
                  ),
              ),
            ),
            FloatingActionButton(onPressed: () async {
              final picked = await showTimePicker(
              context: context, 
              initialTime: _time ?? TimeOfDay.now()
              );
              if (picked != null) {
                setState(() {
                  _time = picked;
                  _timeController.text = picked.format(context);
                });
              }
          }
            ),
              ]
          ),
          Row(children: [
            Expanded(child: TextFormField(
              controller: _idController,
              decoration: const InputDecoration(hintText: 'DriverID'),
              keyboardType: TextInputType.number,
            ))
          ],),
          /*TextFormField(
            decoration: const InputDecoration(hintText: 'something'),
          ),
          */
          ElevatedButton(
              onPressed: () {
                if (_time != null) {
                  submit(_time!, int.parse(_idController.text));
                }
              },
              child: const Text('Submit'),
            )
          ,
        ],
      ),
    );
  }
}