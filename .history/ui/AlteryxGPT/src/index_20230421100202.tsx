import React, { useContext, useState, useEffect } from 'react';
import {
  AyxAppWrapper,
  Button,
  Box,
  TextField,
  Grid,
  Typography,
  makeStyles,
  Select,
  MenuItem,
} from '@alteryx/ui';
import { Context as UiSdkContext } from '@alteryx/react-comms';

const useStyles = makeStyles(() => ({
  formControl: {
    minWidth: '100%',
  },
}));
// App Component
const App = () => {
  const classes = useStyles();
  const { model, handleUpdateModel, getInputMetadata } = useContext(UiSdkContext);

  // Input state
  const [apiKey, setApiKey] = useState('');
  const [inputColumn, setInputColumn] = useState('');
  const [optionalInput, setOptionalInput] = useState('');
  const [classificationAttributes, setClassificationAttributes] = useState('');
  const [promptFormat, setPromptFormat] = useState('');
  const [outputFormat, setOutputFormat] = useState('');

  // Input columns state
  const [inputColumns, setInputColumns] = useState([]);

  // Fetch input columns on initial render
  useEffect(() => {
    async function fetchInputColumns() {
      const inputMetadata = await getInputMetadata();
      const columns = inputMetadata[Object.keys(inputMetadata)[0]].columns;
      setInputColumns(Object.keys(columns));
    }
    fetchInputColumns();
  }, [getInputMetadata]);

  // Submit function for updating model
  const handleSubmit = () => {
    handleUpdateModel({
      ...model,
      ApiKey: apiKey,
      InputColumn: inputColumn,
      OptionalInput: optionalInput,
      ClassificationAttributes: classificationAttributes,
      PromptFormat: promptFormat,
      OutputFormat: outputFormat,
    });
  };

  // Render UI elements
  return (
    <Box p={4}>
      <Grid container spacing={4} direction="column">
        <Grid item>
          <TextField
            label="API Key"
            value={apiKey}
            onChange={(e) => setApiKey(e.target.value)}
            fullWidth
          />
        </Grid>
        <Grid item>
          <Select
            label="Input Column"
            value={inputColumn}
            onChange={(e) => setInputColumn(e.target.value)}
            fullWidth
            className={classes.formControl}
          >
            {inputColumns.map((column) => (
              <MenuItem key={column} value={column}>
                {column}
              </MenuItem>
            ))}
          </Select>
        </Grid>
        <Grid item>
          <Select
            label="Optional Input"
            value={optionalInput}
            onChange={(e) => setOptionalInput(e.target.value)}
            fullWidth
            className={classes.formControl}
          >
            {inputColumns.map((column) => (
              <MenuItem key={column} value={column}>
                {column}
              </MenuItem>
            ))}
          </Select>
        </Grid>
        <Grid item>
          <TextField
            label="Classification Attributes"
            value={classificationAttributes}
            onChange={(e) => setClassificationAttributes(e.target.value)}
            fullWidth
          />
        </Grid>
        <Grid item>
          <TextField
            label="Prompt Format"
            value={promptFormat}
            onChange={(e) => setPromptFormat(e.target.value)}
            fullWidth
          />
        </Grid>
        <Grid item>
          <TextField
            label="Output Format"
            value={outputFormat}
            onChange={(e) => setOutputFormat(e.target.value)}
            fullWidth
          />
        </Grid>
        <Grid item>
          <Button variant="contained" color="primary" onClick={handleSubmit}>
            Submit
          </Button>
        </Grid>
      </Grid>
    </Box>
  );
};

// Tool Component
const Tool = () => {
  return (
    <DesignerApi messages={{}}>
      <AyxAppWrapper>
        <App />
      </AyxAppWrapper>
    </DesignerApi>
  );
};

// Render Tool Component to the DOM
ReactDOM.render(<Tool />, document.getElementById('app'));
