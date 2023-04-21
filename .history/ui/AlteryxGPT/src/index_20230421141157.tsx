
import React, { useEffect, useState } from 'react';
import ReactDOM from 'react-dom';
import AlteryxGuiWrapper, { AlteryxToolType } from '@alteryx/react-comms';
import Alteryx from '@alteryx/alphapack/Alteryx';


const App = () => {
  const [toolConfiguration, setToolConfiguration] = useState<AlteryxToolType>({ ToolID: '', ToolXML: '' });
  const [apiKey, setApiKey] = useState('');
  const [prompt, setPrompt] = useState('');
  const [outputFormat, setOutputFormat] = useState('');
  const [classifyOrAttributes, setClassifyOrAttributes] = useState('Classify');

  useEffect(() => {
    if (toolConfiguration.ToolID) {
      const config = {
        apiKey: apiKey,
        prompt: prompt,
        outputFormat: outputFormat,
        classifyOrAttributes: classifyOrAttributes,
      };

      Alteryx.Gui.Manager.SetConfiguration(encodeURIComponent(JSON.stringify(config)));
    }
  }, [toolConfiguration, apiKey, prompt, outputFormat, classifyOrAttributes]);

  return (
    <div className="App">
      <div>
        <label htmlFor="apiKey">API Key:</label>
        <input
          type="text"
          id="apiKey"
          value={apiKey}
          onChange={(e) => setApiKey(e.target.value)}
        />
      </div>
      <div>
        <label htmlFor="prompt">Prompt:</label>
        <input
          type="text"
          id="prompt"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
        />
      </div>
      <div>
        <label htmlFor="outputFormat">Output Format:</label>
        <input
          type="text"
          id="outputFormat"
          value={outputFormat}
          onChange={(e) => setOutputFormat(e.target.value)}
        />
      </div>
      <div>
        <label htmlFor="classifyOrAttributes">Action:</label>
        <select
          id="classifyOrAttributes"
          value={classifyOrAttributes}
          onChange={(e) => setClassifyOrAttributes(e.target.value)}
        >
          <option value="Classify">Classify</option>
          <option value="Attributes">Attributes</option>
        </select>
      </div>
    </div>
  );
};

Alteryx.Gui.BeforeLoad = (manager: any, AlteryxDataItems: any) => {
  const configString = decodeURIComponent(manager.GetConfiguration());
  const config = configString ? JSON.parse(configString) : {};

  ReactDOM.render(
    <App
      apiKey={config.apiKey || ''}
      prompt={config.prompt || ''}
      outputFormat={config.outputFormat || ''}
      classifyOrAttributes={config.classifyOrAttributes || 'Classify'}
    />,
    document.getElementById('root')
  );
};

Alteryx.Gui.AfterLoad = (manager: any) => {
  manager.AddPropertyEditor('apiKey', 'String');
  manager.AddPropertyEditor('prompt', 'String');
  manager.AddPropertyEditor('outputFormat', 'String');
  manager.AddPropertyEditor('classifyOrAttributes', 'String');
};

Alteryx.Gui.Annotation = () => {
  const configString = decodeURIComponent(Alteryx.Gui.Manager.GetConfiguration());
  const config = configString ? JSON.parse(configString) : {};

  return `GPT Tool (${config.classifyOrAttributes})`;
};

ReactDOM.render(<AlteryxGuiWrapper />, document.getElementById('root'));

