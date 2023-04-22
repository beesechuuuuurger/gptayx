import { Alteryx } from '@alteryx/ui';
import React, { useState } from 'react';
import ReactDOM from 'react-dom';
import { Input, Button, Form, NumericStepper, Select, SelectOption } from '@alteryx/ui';

import './index.scss';

const App = () => {
  const [apiKey, setApiKey] = useState('');
  const [prompt, setPrompt] = useState('');
  const [outputFormat, setOutputFormat] = useState('');
  const [classificationContext, setClassificationContext] = useState('');
  const [columnSelection, setColumnSelection] = useState('');
  const [outputColumns, setOutputColumns] = useState(1);
  const [classificationType, setClassificationType] = useState('classify');

  const handleSubmit = () => {
    Alteryx.Engine.sendDataToPython({
      apiKey,
      prompt,
      outputFormat,
      classificationContext,
      columnSelection,
      outputColumns,
      classificationType
    });
  };


  return (
    <div className="app">
      <Form onSubmit={handleSubmit}>
        <Input
          id="apiKey"
          label="API Key"
          value={apiKey}
          onChange={e => setApiKey(e.target.value)}
        />
        <Input
          id="prompt"
          label="Prompt"
          value={prompt}
          onChange={e => setPrompt(e.target.value)}
        />
        <Input
          id="outputFormat"
          label="Output Format"
          value={outputFormat}
          onChange={e => setOutputFormat(e.target.value)}
        />
        <Input
          id="classificationContext"
          label="Classification Context"
          value={classificationContext}
          onChange={e => setClassificationContext(e.target.value)}
        />
        <Select
          id="columnSelection"
          label="Column Selection"
          onChange={setColumnSelection}
          value={columnSelection}
        >
          {/* Replace these options with your actual column names */}
          <SelectOption value="col1">Column 1</SelectOption>
          <SelectOption value="col2">Column 2</SelectOption>
          <SelectOption value="col3">Column 3</SelectOption>
        </Select>
        <NumericStepper
          id="outputColumns"
          label="Output Columns"
          value={outputColumns}
          onChange={setOutputColumns}
          minValue={1}
          maxValue={3}
        />
        <Select
          id="classificationType"
          label="Classification Type"
          onChange={setClassificationType}
          value={classificationType}
        >
          <SelectOption value="classify">Classify</SelectOption>
          <SelectOption value="list_attributes">List Attributes</SelectOption>
        </Select>
        <Button type="submit">Submit</Button>
      </Form>
    </div>
  );
};

ReactDOM.render(<App />, document.getElementById('root'));
